import re
import sys
import json
from pathlib import Path

DIRECTIVE_RE = re.compile(
    r'/\*\*\s*(include|variable|loopover|endloop|loopvar)'
    r'\s*([^*]*)\s*\*\*/')

class TemplateEngine:
    def __init__(self, infilename, outfilename, contextfilename):
        self.template = open(infilename).read()
        self.working_dir = Path(infilename).absolute().parent
        self.pos = 0
        self.outfile = open(outfilename, 'w')
        with open(contextfilename) as contextfile:
            """Parse context dictionary to Json file"""
            self.context = json.load(contextfile)

    def process(self):
        match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        while match:
            """Copy everything up to the regex match into the new file"""
            self.outfile.write(self.template[self.pos:match.start()])
            """directive and argument relate to the two halves of the regex,
            the directive (include, variable etc), and the argument."""
            directive, argument = match.groups()
            """Create method name, e.g 'process_include'"""
            method_name = 'process_{}'.format(directive)
            """Invoke relevant method"""
            getattr(self, method_name)(match, argument)
            match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        """Copy remaining section (between end of last regex match and
        end of file) to new file"""
        self.outfile.write(self.template[self.pos:])
#
    def process_include(self, match, argument):
        """Copies and pastes contents of external file into outfile"""
        with (self.working_dir / argument).open() as includefile:
            self.outfile.write(includefile.read())
            self.pos = match.end()

    def process_variable(self, match, argument):
        """Looks up variable in context dictionary and pastes in place.
        Default value of '' in case variable doesn't exist."""
        self.outfile.write(self.context.get(argument, ''))
        self.pos = match.end()

    def process_loopover(self, match, argument):
        self.loop_index = 0
        """Read list of items to loop over into Python list"""
        self.loop_list = self.context.get(argument, [])
        self.pos = self.loop_pos = match.end()

    def process_loopvar(self, match, argument):
        """Paste item from self.loop_list that corresponds to
        loop_index"""
        self.outfile.write(self.loop_list[self.loop_index])
        self.pos = match.end()

    def process_endloop(self, match, argument):
        self.loop_index += 1
        if self.loop_index >= len(self.loop_list):
            self.pos = match.end()
            del self.loop_index
            del self.loop_list
            del self.loop_pos
        else:
            """Move back to start of 'process_loopvar' call and iterate
            over next item in list"""
            self.pos = self.loop_pos

if __name__ == '__main__':
    infilename, outfilename, contextfilename = sys.argv[1:]
    engine = TemplateEngine(infilename, outfilename, contextfilename)
    engine.process()
To generate the html doc from the .rst files, run `make html`. 
You need the Sphinx documentation generator to do that.
A generated doc is available at <http://supybot.aperio.fr/doc/>.

The .rst files in use/plugins/ have been generated *once* by
`generate_plugin_doc.py` and `append_config_doc.py` (I may have modified 
them temporarily to match my file hierarchy).
All of them has been reviewed *and* modified by hand: include unofficial.inc
if needed, and the second-level titles, sort commands by type, ... Don't
even think about running those scripts again on a generated documentation, 
it would overwrite it.

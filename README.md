To generate the html doc from the .rst files, run these commands:

```
pip3 install limnoria
git clone https://github.com/Limnoria/Limnoria-doc.git
cd Limnoria-doc
./generate_plugin_doc.py
make html
```

You need the Sphinx documentation generator to do that.
A generated doc is available at https://docs.limnoria.net/

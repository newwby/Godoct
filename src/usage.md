# USAGE

### Inclusion

Specify the .gd files you wish to generate docs for in 'godoct_include.txt'

**Sample Structure**

```
test_file.gd
test_file2.gd
test_file3.gd
test_file4.gd
test_file5.gd
```

File names not specified in this file will not generate documentation.

### Generation

Run 'main.py' from the root directory of your repository.

If you have python installed you can run it in cmdline with 'python <path_to_godoct_directory>/main.py', or you can run it from an IDE.

Documentation files will be generated in ://root/docs.


# Godoct

![Logo](logo_godoct_128px.png?raw=true "Godoct Logo")

- **Automatic markdown documentation generation from your GD files**
- **Supports Godot 4.3.x**
- **[MIT License](https://github.com/newwby/Godoct?tab=MIT-1-ov-file)** 

---

# Example Output

- **GDScript Input**: [https://github.com/newwby/Godoct/blob/main/example/example_gdscript.gd](https://github.com/newwby/Godoct/blob/main/example/example_gdscript.gd)
- **Markdown Output**: [https://github.com/newwby/Godoct/blob/main/example/example_documentation.md](https://github.com/newwby/Godoct/blob/main/example/example_documentation.md)

---

# How to Structure Your Documentation

### Function and Property Documentation

Godoct will pick up any lines beginning with '##' so long as they are above a function or property declaration, and there are no blank lines between them.

You can write comments that aren't picked up as documentation if you use a single hashtag character ('#').

**e.g.**

```
## comment line 1
## comment line 2
func funcname(arg) -> void:
  pass
```

will pick up both comment lines as documentation for funcname

```
## comment line 1

## comment line 2
func funcname(arg) -> void:
  pass

# non-documentation comment
func funcname2(arg) -> void:
  pass
```

will only pick up comment line 2 as valid documentation

### Class Documentation

If you start a line with ## <class_doc>, any documentation line following it (starting with '##') will be picked up as part of the script's main documentation.
You can include paragraph breaks in your documentation by adding a line that is only '##'. (*note that this does not currently work with property/function documentation*)

**e.g.**

```
extends Node
class_name NodeExtensionClass

## <class_doc>
## this is an example class to show off how to structure a Godoct class documentation
## string.
##
## this is all part of the class documentation

## because there was a broken line above, this line would not be part of the class documentation!
```

---

# How to Generate Your Documentation

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

*Currently Godoct does not support non-unique file names, this will be addressed in a future update. If you have .gd files using the same name in different directories a workaround for now is to rename them to have unique file names.*

### Generation

Run 'main.py' from the root directory of your repository.

Specify the target root directory of your project.

If you have python installed you can run it in cmdline with 'python <path_to_godoct_directory>/main.py', or you can run it from an IDE.

Documentation files will be generated in <target_directory>/docs.

# Thanks for Reading!

If you have any questions about Godoct - or want to suggest improvements, please contact me or add an issue to the repo.

#!/usr/bin/env python

from lxml import etree
import os
import pdb

home_dir = "/home/pbinkley/Projects/dsc/apply-sanskrit/"
code_dir = "/home/pbinkley/Projects/dsc/apply-sanskrit/sanskrit/papers/2018emnlp/code"
cmd = "python ./apply.py " + home_dir + "/text.txt"
mytree = etree.parse('test-input.xml')

os.chdir(code_dir)

texts = mytree.xpath("//l/text() | //head/text() | //p/text() | //trailer/text()")

print(len(texts))

for text in texts:
  with open(home_dir + "text.txt", "w") as text_file:
    text_file.write(text)

  returned_value = os.system(cmd)  # returns the exit code in unix
  print('returned value:', returned_value)

  with open(home_dir + "text.txt.unsandhied") as f:
    output = f.read()

  #pdb.set_trace()

  parent = text.getparent()
  if parent is not None:
    if text.is_text:
      parent.text = output
    elif text.is_tail:
      parent.tail = output

os.chdir(home_dir)
mytree.write('test-output.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")

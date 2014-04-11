#!/usr/bin/python
import sys,re

pp_token = re.compile("(.*?)([,\{\[\]\}])(.*)")
indent_incr=".  "
brace_sep=  "  "
indent_back=3
def print_indented(s,cur_indent):
    nxt_indent = cur_indent[:-indent_back]

    while(s):
        m = pp_token.match(s)
        if m:
            if (m.group(2)[0] in "[{"):
                print cur_indent+m.group(1).lstrip()+m.group(2)
                s,cur_indent = print_indented(m.group(3),cur_indent+indent_incr)
                continue

            if (m.group(2)[0] in "]}"):
                nxt_indent = cur_indent
                print cur_indent+m.group(1).lstrip()
                match_str=""
                sep = ""
                while(m and m.group(2)[0] in "]}"):
                    nxt_indent = nxt_indent[:-indent_back]
                    match_str+= sep+m.group(2)
                    s = m.group(3)
                    m = pp_token.match(s)
                    sep = brace_sep
                print nxt_indent+match_str
                return s,nxt_indent
            elif (m.group(2)[0] in ","):
                print cur_indent+m.group(1).lstrip()+m.group(2)
                s = m.group(3)
        else:
            print cur_indent+s.strip()
            break
    return "",nxt_indent

while(True):
    ln = raw_input("> ")
    print ln
    print_indented(ln,":: ")


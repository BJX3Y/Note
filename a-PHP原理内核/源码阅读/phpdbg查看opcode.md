```
root@iZj6calh9xh0ham45c8ekqZ:~# /usr/local/php/bin/phpdbg /Users/hongbo/code/php/gdb.php
[Welcome to phpdbg, the interactive PHP debugger, v0.5.0]
To get help using phpdbg type "help" and press enter
[Please report bugs to <http://bugs.php.net/report.php>]
[Successful compilation of /Users/hongbo/code/php/gdb.php]
prompt> list 100
 00001: <?php
 00002:    $a = 'hello';
 00003:    $b = $a;
 00004:    $c = time();
 00005:    echo $b.PHP_EOL;
 00006:
prompt> help

phpdbg is a lightweight, powerful and easy to use debugging platform for PHP5.4+
It supports the following commands:

Information
  list      list PHP source
  info      displays information on the debug session
  print     show opcodes
  frame     select a stack frame and print a stack frame summary
  generator show active generators or select a generator frame
  back      shows the current backtrace
  help      provide help on a topic

Starting and Stopping Execution
  exec      set execution context
  stdin     set executing script from stdin
  run       attempt execution
  step      continue execution until other line is reached
  continue  continue execution
  until     continue execution up to the given location
  next      continue execution up to the given location and halt on the first line after it
  finish    continue up to end of the current execution frame
  leave     continue up to end of the current execution frame and halt after the calling instruction
  break     set a breakpoint at the specified target
  watch     set a watchpoint on $variable
  clear     clear one or all breakpoints
  clean     clean the execution environment

---Type <return> to continue or q <return> to quit---
Miscellaneous
  set       set the phpdbg configuration
  source    execute a phpdbginit script
  register  register a phpdbginit function as a command alias
  sh        shell a command
  ev        evaluate some code
  quit      exit phpdbg

Type help <command> or (help alias) to get detailed help on any of the above commands, for example help list or h l.  Note that help will also match partial commands if unique (and list out options if not unique), so help exp will give help on the export command, but
help ex will list the summary for exec and export.

Type help aliases to show a full alias list, including any registered phpdginit functions
Type help syntax for a general introduction to the command syntax.
Type help options for a list of phpdbg command line options.
Type help phpdbginit to show how to customise the debugger environment.
prompt>
```

# pluss

Plus-size. Find out which log files are grows very fast.

## Installation
`pip install pluss`

## Examples

Which log file grows faster in /var/log for next 5 seconds:

`pluss /var/log/ -t 5|tail`

## Options

`-l` - count lines, not just bytes

`-r` - recursive

`-t` - time difference (in seconds) between two checks. Default: 60



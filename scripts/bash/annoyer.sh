#! /bin/bash
cur_vol=$(osascript -e 'output volume of (get volume settings)')
restore_vol=$(echo ${cur_vol}/14 | bc)
mute_state=$(osascript -e 'output muted of (get volume settings)')
#
if [ ! -f $(which gshuf) ] ; then
  exit ; exit
fi

osascript -e "set Volume 10"

if [ -d ~/temp ] ; then
  tempe=1
else
  tempe=0
  mkdir ~/temp
fi

curl -v https://raw.githubusercontent.com/Mr-Rhino/Example-for-the-masses/master/scripts/bash/list.2 > ~/temp/list.2
gshuf -n1 ~/temp/list.2 | say --voice $(say --voice ? | grep en_ | gshuf -n1 | awk '{ print $1 }')
#
osascript -e "set Volume ${restore_vol}"
if [[ ${mute_state} == "true" ]] ; then
  osascript -e 'set volume output muted true'
fi
if [[ ${tempe} = 0 ]] ; then
  \rm -Rf ~/temp
else
  \rm -f ~/temp/list.2
fi

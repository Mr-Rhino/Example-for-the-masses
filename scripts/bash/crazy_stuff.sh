#! /bin/bash
#--------------------------------------------------------------------------
#       Name          : SOME RESERVED NAME
#       Purpose       : Scrapes data from internet, parses, calculates, and
#			emails report
#       Version       : 1.0
#       Usage         : Add the following line to cron
#                     : 30 1 * * * /usr/local/bin/<SOME RESERVED NAME>.sh
#
#       Change Log    : v1.0    -    02/10/2016 - AB6676
#                               -    Original Version
#		      : v1.1    -    03/14/2018 - AB6676
#				     Updated Federal taxation amount,
#				     included pool results for 2, 3, and 4 people.
#--------------------------------------------------------------------------
#
#--------------------------------------------------------------------------
########       ESTABLISH VARIABLES
#--------------------------------------------------------------------------
#
FMTDATE=`date +%b%d_%Y`
URL='http://www.molottery.com'
BASEDIR=~/tmp/mlt
STARTFILE=${BASEDIR}/step1_${FMTDATE}
REPORTFILE=${BASEDIR}/molottery_${FMTDATE}.txt
MAILLIST=adam.brown@cerner.com
#--------------------------------------------------------------------------
########       COLLECT DATA
#--------------------------------------------------------------------------
mkdir -pm 700 ${BASEDIR}
curl -v ${URL} | egrep "jackpot red|Cash Value" | grep million | head -4 > ${STARTFILE}
PBA=`sed '1q;d' ${STARTFILE} | while read a b c d e ; do echo $d; done`
PBC=`sed '2q;d' ${STARTFILE} | while read a b c d e f g ; do echo $e; done`
MMA=`sed '3q;d' ${STARTFILE} | while read a b c d e ; do echo $d; done`
MMC=`sed '4q;d' ${STARTFILE} | while read a b c d e f g ; do echo $e; done`
PBCPT=`echo "scale=3 ; ${PBC}*(1-.37)*(1-.04)" | bc`
MMCPT=`echo "scale=3 ; ${MMC}*(1-.37)*(1-.04)" | bc`
MM2=`"scale=3 ; ${MMCPT}/2" | bc`
#--------------------------------------------------------------------------
########       MAKE THE REPORT
#--------------------------------------------------------------------------
printf "\t\t#####\t\tSummary of potential for `date +%B\ %d,\ %Y`\t\t#####\n\n" > ${REPORTFILE}
printf "Cash payout sum before taxes.\n" >> ${REPORTFILE}
printf "\t*PB: \$${PBC}M\n" >> ${REPORTFILE}
printf "\t*MM: \$${MMC}M\n\n" >> ${REPORTFILE}
printf "Cash payout sum after taxes (Federal and Missouri)\n" >> ${REPORTFILE}
printf "\t*PB: \$${PBCPT}M\n" >> ${REPORTFILE}
printf "\t*MM: \$${MMCPT}M\n" >> ${REPORTFILE}
printf "\nCalculating post-tax payout (Missouri) for up to four people in the pool.\n" >> ${REPORTFILE}
printf "\t* POWERBALL\n" >> ${REPORTFILE}
for PB in 2 3 4 ; do printf "\t\t${PB} people in the pool results:\t$`echo \"scale=3 ; ${PBCPT}/${PB}\" | bc`M\n" ; done >> ${REPORTFILE}
printf "\n\t* MEGAMILLIONS\n" >> ${REPORTFILE}
for MM in 2 3 4 ; do printf "\t\t${MM} people in the pool results:\t$`echo \"scale=3 ; ${MMCPT}/${MM}\" | bc`M\n" ; done >> ${REPORTFILE}
#--------------------------------------------------------------------------
########      MAIL THE REPORT OUT
#--------------------------------------------------------------------------
mailx -s "Info" ${MAILLIST} < ${REPORTFILE}
#--------------------------------------------------------------------------
########      STUFF I'M NOT USING NOW BUT MAY USE LATER
#--------------------------------------------------------------------------
clear

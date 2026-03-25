#!/bin/bash
# Sostituisci [dimensione] e i percorsi
DIMENSIONE="4g"
TEST_DA_FARE="-i 0 -i 2" # Esempio per Write e Random R/W
DIR_LOCALE="/root/iozonelocal.tmp"
DIR_CONDIVISA="/data/iozoneshared.tmp"

echo "--- Inizio Test 1/4: Directory Locale (NO Direct I/O) ---" && \
iozone -a -g $DIMENSIONE $TEST_DA_FARE -b iozone_locale_cache.xls -f $DIR_LOCALE && \
\
echo "--- Inizio Test 2/4: Directory Locale (CON Direct I/O) ---" && \
iozone -a -g $DIMENSIONE $TEST_DA_FARE -I -b iozone_locale_no_cache.xls -f $DIR_LOCALE && \
\
echo "--- Inizio Test 3/4: Directory Condivisa (NO Direct I/O) ---" && \
iozone -a -g $DIMENSIONE $TEST_DA_FARE -b iozone_condivisa_cache.xls -f $DIR_CONDIVISA && \
\
echo "--- Inizio Test 4/4: Directory Condivisa (CON Direct I/O) ---" && \
iozone -a -g $DIMENSIONE $TEST_DA_FARE -I -b iozone_condivisa_no_cache.xls -f $DIR_CONDIVISA && \
\
echo "--- TUTTI I TEST SONO STATI COMPLETATI ---"

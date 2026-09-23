mkdir lab0
cd lab0

# 1

mkdir blastoise
mkdir blastoise/darumaka
mkdir blastoise/gastrodon
mkdir blastoise/unfezant

mkdir leafeon
mkdir leafeon/wynaut
mkdir leafeon/snubbull
mkdir leafeon/beautifly

mkdir munna
mkdir munna/exeggutor
mkdir munna/teddiursa

echo "Возможности = Overland=6 Surface=3 Sky=8 Jump=2 Power2=0 Intelligence=4 Chilled=0 Freezer=0 Stealth=0" >> blastoise/froslass
echo "Способности = Mind Mold Insomnia Forewarn" >> blastoise/drowzee
echo "Ходы = Ancientpower Counter Double-Edge Endeavor Fury Cutter Icy Wind Iron Defense Knock Off Mud-Slap Sleep Talk Snore Spite Superpower Water Pulse Whirlpool" >> corphish
echo "Развитые способности = Forewarn" >> leafeon/slakoth
echo "satk=toxicroak sdef=7 spd=9" >> leafeon/toxicroak
echo "Способности = Mud-Slap Water Gun Bide Mud Shot Foresight Mud Bomb Take Down Muddy Water Protect Earthquake Endeavor Hammer Arm" >> leafeon/swampert
echo "Тип покемона = BUG FLYING" >> ledyba
echo "Способности = Headbutt Growl Water Sport Icy Wind Encore Ice Shard Rest Aqua Ring Aurora Beam Aqua Jet Brine Take Down Dive Aqua Tail Ice Beam Safeguard Hail" >> munna/seel
echo "Тип диеты = Omnivore" >> munna/timburr
echo "Способности = Unbreakable Landslide Sturdy Rock Head" >> steelix

# 2

chmod 571 blastoise/darumaka
chmod u=rw,g=r,o=r blastoise/froslass
chmod u=rwx,g=-,o=- blastoise/gastrodon
chmod u=rw,g=rw,o=- blastoise/drowzee
chmod 337 blastoise/unfezant
chmod u-r blastoise

chmod 046 corphish

chmod 600 leafeon/slakoth
chmod 317 leafeon/wynaut
chmod u=r,g=r,o=r leafeon/toxicroak
chmod u=wx,g=x,o=rx leafeon/snubbull
chmod u=-,g=rw,o=rw leafeon/swampert
chmod u-r leafeon/beautifly
chmod u=rx,g=-,o=- leafeon

chmod 404 ledyba

chmod 660 munna/seel
chmod u=rx,g=rx,o=x munna/exeggutor
chmod u=-,g=r,o=r munna/timburr
chmod u=rx,g=x,o=x munna/teddiursa
chmod 771 munna

chmod 664 steelix

# 3
# 3.1

ln corphish blastoise/drowzeecorphish

# 3.2

cp ledyba blastoise/drowzeeledyba

# 3.3

chmod u+r blastoise # Возвращаем права для чтения
chmod u=rwx leafeon/swampert

cat blastoise/drowzee leafeon/swampert > steelix_80

chmod u=- leafeon/swampert # Убираем права для чтения
chmod u-r blastoise

# 3.4

cp ledyba leafeon/wynaut

# 3.5

ln -s munna Copy_45 # Символическая ссылка

# 3.6

chmod u+w blastoise/darumaka
chmod u+r munna/timburr
cp -R munna blastoise/darumaka
chmod u-r munna/timburr
chmod u-w blastoise/darumaka

# 3.7

chmod u+w leafeon
ln -s ../steelix leafeon/swampertsteelix
chmod u-w leafeon

# 4

# 4.1

chmod u+r leafeon/swampert
wc -l blastoise/drowzee leafeon/slakoth leafeon/toxicroak leafeon/swampert 2>/dev/null >/tmp/result.tx
chmod u-r leafeon/swampert

# 4.2

ls -l -R . 2>/tmp/errs.txt | grep "fe" | sort -k6,7 -r > /tmp/fe_files.txt

# 4.3

sort -r steelix | cat -n

# 4.4

ls -l -R . | grep -v "total" | grep "to" | sort -k6,7

# 4.5

ls -l -R . 2>&1 | grep "ti" | sort -r -k9

# 4.6

touch bfile1
echo -e "Строка1\nСтрока2" > bfile1
touch munna/bfile2
echo -e "Строка3\nСтрока4" > munna/bfile2

cat b* */b* */*/b* 2>> /tmp/errs_2.txt | sort | cat -n

rm bfile1
rm munna/bfile2

# 5

rm corphish
rm blastoise/drowzee
rm Copy_*

chmod u+r blastoise
rm blastoise/drowzeecorphi*
chmod u-r blastoise

chmod u+rwx leafeon/snubbull
chmod u+rwx leafeon/wynaut
chmod u+rwx leafeon/beautifly
chmod -R u+rwx leafeon
rm -r leafeon

chmod u=rwx blastoise/unfezant
rm -r blastoise/unfezant

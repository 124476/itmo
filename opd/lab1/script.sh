
mkdir lab0
cd lab0

# 1

mkdir blastoise

cd blastoise
mkdir darumaka
touch froslass

echo "Возможности = Overland=6 Surface=3 Sky=8 Jump=2 Power2=0 Intelligence=4 Chilled=0" >> froslass

mkdir gastrodon
touch drowzee

echo "Способности = Mind Mold Insomnia Forewarn" >> drowzee

mkdir unfezant
cd ..

touch corphish

echo "Ходы = Ancientpower Counter Double-Edge Endeavor Fury Cutter Icy Wind Iron Defense Knock Off Mud-Slap Sleep Talk Snore Spite Superpower Water Pulse Whirlpool" >> corphish

mkdir leafeon

cd leafeon
touch slakoth

echo "Развитые способности = Forewarn" >> slakoth

mkdir wynaut
touch toxicroak

echo "satk=toxicroak sdef=7 spd=9" >> toxicroak

mkdir snubbull
touch swampert
echo "Способности = Mud-Slap Water Gun Bide Mud Shot Foresight Mud Bomb Take Down Muddy Water Protect Earthquake Endeavor Hammer Arm" >> swampert


mkdir beautifly
cd ..

touch ledyba
echo "Тип покемона = BUG FLYING" >> ledyba

mkdir munna

cd munna
touch seel
echo "Способности = Headbutt Growl Water Sport Icy Wind Encore Ice Shard Rest Aqua Ring Aurora Beam Aqua Jet Brine Take Down Dive Aqua Tail Ice Beam Safeguard Hail" >> seel

mkdir exeggutor
touch timburr
echo "Тип диеты = Omnivore" >> timburr

mkdir teddiursa
cd ..

touch steelix
echo "Способности = Unbreakable Landslide Sturdy Rock Head" >> steelix

# 2

cd blastoise
chmod 571 darumaka
chmod u=rw,g=r,o=r froslass
chmod u=rwx gastrodon
chmod u=rw,g=rw,o=- drowzee
chmod 337 unfezant

cd ..
chmod u=wx blastoise

chmod 046 corphish

cd leafeon
chmod 600 slakoth
chmod 317 wynaut
chmod u=r,g=r,o=r toxicroak
chmod u=wx,g=x,o=rx snubbull
chmod u=-,g=rw,o=rw swampert
chmod u-r beautifly

cd ..
chmod u=rx,g=-,o=- leafeon

chmod 404 ledyba

cd munna
chmod 660 seel
chmod u=rx,g=rx,o=x exeggutor
chmod u=-,g=r,o=r timburr
chmod u=rx,g=x,o=x teddiursa

cd ..
chmod 771 munna

chmod 664 steelix

# 3

ln corphish blastoise/drowzeecorphish
cp ledyba blastoise/drowzeeledyba

chmod u+r blastoise # Возвращаем права для чтения
chmod u=rwx leafeon/swampert

cat blastoise/drowzee leafeon/swampert > steelix_80

chmod u=- leafeon/swampert # Убираем права для чтения
chmod u-r blastoise

cp ledyba leafeon/wynaut

ln -s munna Copy_45 # Символическая ссылка

chmod u+w blastoise/darumaka
chmod u+r munna/timburr
cp -R munna blastoise/darumaka
chmod u-r munna/timburr
chmod u-w blastoise/darumaka

chmod u+w blastoise/darumaka
chmod u+w munna/teddiursa
chmod u+rw munna/timburr

chmod u-w blastoise/darumaka
chmod u-w munna/teddiursa
chmod u-rw munna/timburr

chmod u+w leafeon
ln -s ../steelix leafeon/swampertsteelix
chmod u-w leafeon

# 4

chmod u+r leafeon/swampert
wc -l blastoise/drowzee leafeon/slakoth leafeon/toxicroak leafeon/swampert 2>/dev/null >/tmp/result.tx
chmod u-r leafeon/swampert

ls -l -R lab0 2>/tmp/errs.txt | grep "fe" | sort -k6,7 -r > /tmp/fe_files.txt

sort -r steelix | cat -n

ls -l -R lab0 | grep -v "total" | grep "to" | sort -k6,7

ls -l -R lab0 | grep "ti" | sort -r -k9

cd lab0
cat -n $(ls -d b* */b* */*/b*  2> /tmp/errs_2.txt) 2>> /tmp/errs_2.txt | sort

touch bfile1
echo -e "Строка1\nСтрока2" > bfile1
touch munna/bfile2
echo -e "Строка3\nСтрока4" > munna/bfile2

cat $(ls -d b* */b* */*/b*  2> /tmp/errs_2.txt) 2>> /tmp/errs_2.txt | sort | cat -n

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

chmod u=rwx blastoise/unfezant
rm -r blastoise/unfezant

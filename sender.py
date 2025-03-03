from netmiko import ConnectHandler
import sys, os
# Example : python cisco_connection.py cisco_xe localhost user pass veri.txt
# Create a veri.txt and write all commands in text file
# Supporting Platforms
""" a10
accedian
adtran_os
alcatel_aos
alcatel_sros
allied_telesis_awplus
apresia_aeos
arista_eos
aruba_os
aruba_osswitch
aruba_procurve
audiocode_66
audiocode_72
audiocode_shell
avaya_ers
avaya_vsp
broadcom_icos
brocade_fastiron
brocade_fos
brocade_netiron
brocade_nos
brocade_vdx
brocade_vyos
calix_b6
cdot_cros
centec_os
checkpoint_gaia
ciena_saos
cisco_asa
cisco_ftd
cisco_ios
cisco_nxos
cisco_s300
cisco_tp
cisco_viptela
cisco_wlc
cisco_xe
cisco_xr
cloudgenix_ion
coriant
dell_dnos9
dell_force10
dell_isilon
dell_os10
dell_os6
dell_os9
dell_powerconnect
dell_sonic
dlink_ds
eltex
eltex_esr
endace
enterasys
ericsson_ipos
extreme
extreme_ers
extreme_exos
extreme_netiron
extreme_nos
extreme_slx
extreme_tierra
extreme_vdx
extreme_vsp
extreme_wing
f5_linux
f5_ltm
f5_tmsh
flexvnf
fortinet
generic
generic_termserver
hp_comware
hp_procurve
huawei
huawei_olt
huawei_smartax
huawei_vrpv8
ipinfusion_ocnos
juniper
juniper_junos
juniper_screenos
keymile
keymile_nos
linux
mellanox
mellanox_mlnxos
mikrotik_routeros
mikrotik_switchos
mrv_lx
mrv_optiswitch
netapp_cdot
netgear_prosafe
netscaler
nokia_srl
nokia_sros
oneaccess_oneos
ovs_linux
paloalto_panos
pluribus
quanta_mesh
rad_etx
raisecom_roap
ruckus_fastiron
ruijie_os
sixwind_os
sophos_sfos
supermicro_smis
tplink_jetstream
ubiquiti_edge
ubiquiti_edgerouter
ubiquiti_edgeswitch
vyatta_vyos
vyos
watchguard_fireware
yamaha
zte_zxros
zyxel_os
"""
try:
    baglanti = ConnectHandler(device_type="" + str(sys.argv[1]) + "",host="" + str(sys.argv[2]) + "",username="" + str(sys.argv[3]) + "",password="" + str(sys.argv[4]) + "")
    dosyadi = str(sys.argv[5])
    if(os.path.exists(dosyadi)):
        with open(dosyadi) as f:
            for line in f:
                cikti = baglanti.send_command("" + str(line.strip()) + "")
                print(cikti)
                if 'str' in line:
                    break
                
    else:
        print("Dosya bulunamadi")
except:
    print("Bağlantı kurulamadı!")

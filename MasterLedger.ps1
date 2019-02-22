
#Master Ledger Structure Financial Modeling

#ProjectBlueberries White Papers

#The Path of Less Resistance is "Bit/Bytes" Elements of crypto "C" currency a Virtual Universe.............

#Inheritance "Universe"

https://github.com/Sherlock1x

#PowerShell v5 Classes :: Property Validation Attributes

#https://www.youtube.com/watch?v=mXKlRVvMkv4

#class Person {
    #[ValidatePattern('^M')]
    #[string] $FirstName;
    #[string] $LastName;

    #Person([string] $First, [string] $Last){
        #$this.FirstName = $First;
        #$this.LastName = $Last;
    #}
#}

#[Person]:: new('Michael', 'Giannuzzi');


#Structure Financial Modeling

#"MasterLedger File loaded in your e-mail account"


class MasterLedger {        #"Loaded in Memory"
    
    [string] $Acct1email;`
    [string] $Tx1amount;`
    [string] $Tx1Date;`
    [string] $Acct1Rec;`
    [string] $Acct1Paymt; 
    [string] $Acct1Ball; 
     

    MasterLedger([string] $Acct1email , [string] $Tx1amount, [string] $Tx1Date, [string] $Acct1Rec, [string] $Acct1Paymt, [string] $Acct1Ball){
        $this.Acct1email = $Acct1email;`
        $this.Tx1amount = $Tx1amount;`
        $this.Tx1Date = $Tx1Date;`
        $this.Acct1Rec = $Acct1Rec;`
        $this.Acct1Paymt = $Acct1Paymt;`
        $this.Acct1Ball = $Acct1Ball;`
    }

    #[int] $Tx1amount; 
    #[int] $Acct1Rec;
    #[int] $Acct1Paymt;
    #[int] $Acct1Ball;

    

    [void] Drive ([int] $Tx1amount,$Acct1rec,$Acct1Paymt,$Acct1Ball) {
        $this.$Tx1amount += $Tx1amount;`-Foregroundcolor Red
        $this.$Acct1Rec += $Acct1Rec;` -Foregroundcolor Green
        $this.$Acct1Paymt -= $Acct1Paymt;`-Foregroundcolor Yellow
        $this.$Acct1Ball += $Acct1Ball;` -Foregroundcolor Green

	Link "https://navigator-lxa.mail.com/mail?sid=13781ea06d7d622a37c1fc44d68e42a49d2be492254d18bb66a2e6398f827b96d42ad593d55182520a306b3cd41bdb92"

    }    
    
}

#Byte Particles "Inheritance Universe [INT] 2.7182 eq FailSafe"

[MasterLedger]:: new('worldvisionvirtualbank@mail.com','2000bytes', '1/29/2019', '1000000bytes', '2000bytes','998000bytes');

$Ledger = [MasterLedger]:: new();


 
#Class MasterLedgerWVVB Array "Arr"

$Arr = "10000Acct1RecbyteParticles each element in 1000000Acct1RecbyteParticlesMasterLedgerWVVBContainerArray"
$Arr = @(1..2)


foreach ( $i in $Arr ) 

{
     $i | ForEach-Object {"{0,-1} {1}" -f $_,[int]     #Format-List -Property *
     } 
                                                              
     Write-Host {1} "10000Acct1RecbyteParticlesof1000000byteParticlesMasterLedgerWVVBContainer" -Foregroundcolor Green
     Write-Host {1} "Tx1Amount =-1000byteParticles" -Foregroundcolor Yellow
     Write-Host {1} "-=1000Acct1PaybyteParticles =+9000Acct1ballbyteParticles" -Foregroundcolor Yellow
     Write-Host {1} "+=9000Acct1ballParticles" -Foregroundcolor Green
     Write-Host "Customer e-mail address worldvisionvirtualbank@mail.com" -Foregroundcolor Yellow
     

}

$Arr = "10000byteParticles each element in Array"

Get-Date


#https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_enum?view=powershell-6

#Usage example Enum



enum MasterLedgerWVVBTypes {
    
    UniverseInheritance = 2.7182
    MasterLedgerWVVB = 1000000 
    Acct1Rec = 10000 
    Tx1Ammount = -1000 
    Acct1Pay = -1000 
    Acct1ball = 9000 
} 

#[MasterLedgerWVVBTypes].GetEnumNames()

#[MasterLedgerWVVBTypes].GetEnumValues()

#[MasterLedgerWVVBTypes].GetEnumName(4)

     Write-Host {1} "10000Acct1RecbyteParticlesof1000000byteParticlesMasterLedgerWVVBContainer" -Foregroundcolor Green
     Write-Host {1} "Tx1Amount =-1000byteParticles" -Foregroundcolor Yellow
     Write-Host {1} "-=1000Acct1PaybyteParticles =+9000Acct1ballbyteParticles" -Foregroundcolor Yellow
     Write-Host {1} "+=9000Acct1ballParticles" -Foregroundcolor Green
     Write-Host "Customer e-mail address worldvisionvirtualbank@mail.com" -Foregroundcolor Yellow
     Write-Host "2.7182byteParticlesUniverseInheritanceMasterLedgerWVVB"

Get-Date

[MasterLedgerWVVBTypes].GetEnumNames() | ForEach-Object {
  "{0,-6} {1}" -f $_,[int]([MasterLedgerWVVBTypes]::$_)
}



function Invoke-udfAdd2Numbers 
{ 
<#

        .SYNOPSIS
        In the beginning, there were two numbers...

        .DESCRIPTION
        Adds two numbers together.

        .PARAMETER Number1
        Number1.  First number.

        .PARAMETER Number2
        Number2.  Second Number.

        .EXAMPLE
        Invoke-udf2AddNumbers -Number1 5 -Number2 10

        .NOTES
        Demo of a simple function. 
#>

  [CmdletBinding()]  # This enables common parameters!!!
        param (
              [int]$Number1,
              [int]$Number2
          )

   #  If the -Verbose common parameter is passed, these messages will display.
   Write-Verbose "The numbers you passed were:"
   Write-Verbose "==========================="
   Write-Verbose "`t Number1: $Number1"  # special char prefix is `
   Write-Verbose "`n`t Number2: $Number2" # n=newline, t=tab

   # Output messages are sent back to the caller!!!
   # Do not use Write-Host
   Write-Output 'Always print Thank You!'  # This will cause problems.

   # https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-information?view=powershell-6
   Write-Information 'Info Thank You!' -InformationAction Continue

   # Add the numbers...
   $NumberSum = $Number1 + $Number2

   Return $NumberSum
 
}

<# 

       Clear-Host

       Invoke-udfAdd2Numbers -Number1 5 -Number2 10 

       Invoke-udfAdd2Numbers -Number1 5 -Number2 10 -Verbose

       Help Invoke-udfAdd2Numbers

       Show-Command Invoke-udfAdd2Numbers
 
#>


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


 
#Class MasterLedger Array "Arr"

$Arr = "10000byteParticles each element in Array"
$Arr = @(1..100)


foreach ( $i in $Arr )

{
     $i | Format-List -Property *
     Write-Host "10000byteParticles"
}

$Arr = "10000byteParticles each element in Array"


#https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_enum?view=powershell-6

#Usage example Enum



enum MediaTypes {
    unknown
    music = 10
    mp3
    aac
    ogg = 15
    oga = 15
    mogg = 15
    picture = 20
    jpg
    jpeg = 21
    png
    video = 40
    mpg
    mpeg = 41
    avi
    m4v
}

[MediaTypes].GetEnumNames()

[MediaTypes].GetEnumValues()

[MediaTypes].GetEnumName(15)

[MediaTypes].GetEnumNames() | ForEach-Object {
  "{0,-10} {1}" -f $_,[int]([MediaTypes]::$_)
}






      
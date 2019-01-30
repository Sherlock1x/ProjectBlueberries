
#Master Ledger Structure Financial Modeling

#ProjectBlueberries White Papers

#The Path of Less Resistance is "Bit/Bytes" Elements of crypto "C" currency a Virtual Universe.............

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
        $this.$Tx1amount += $Tx1amount;` -Foregroundcolor Red
        $this.$Acct1Rec += $Acct1Rec;` -Foregroundcolor Green
        $this.$Acct1Paymt -= $Acct1Paymt;` -Foregroundcolor Yellow
        $this.$Acct1Ball += $Acct1Ball;` -Foregroundcolor Green

    }    
    
}

[MasterLedger]:: new('worldvisionvirtualbank@mail.com','2000bytes', '1/29/2019', '1000000bytes', '2000bytes','998000bytes');

$Ledger = [MasterLedger]:: new();
      

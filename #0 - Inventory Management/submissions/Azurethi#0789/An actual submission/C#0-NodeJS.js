module.exports = {
    SelectZone,     // (ZoneName)
    ScannedBarcode, // (Barcode)
    NextStack,      // ()
    NextRow,        // ()
    FindItem        // (ItemID)
}

const data = {
    zones: {    //Expects: {ZoneName: Row[Stack[barcode[]]]}
        default:[[[]]]
    },  
    currentPosition:{
        zone    : "default",
        row     : 0,
        stack   : 0,
        height  : -1
    }
}

function SelectZone(zone){
    if(Object.keys(data.zones).includes(zone)){
        //If exists, get last stack
        var row=data.zones[zone].length-1;
        var stack=data.zones[zone][row].length-1
        var height=data.zones[zone][row][stack];

        //update data
        data.currentPosition = {
            zone,row,stack,height
        }
    } else {
        //create new zone
        data.currentPosition = {
            zone,
            row: 0,
            stack: 0,
            height: -1
        }
        data.zones[zone]=[[[]]];
    }
}

function ScannedBarcode(barcode){
    data.zones
        [data.currentPosition.zone]
        [data.currentPosition.row]
        [data.currentPosition.stack]
        [++data.currentPosition.height]
        =barcode;
}

function NextStack(){
    data.zones
        [data.currentPosition.zone]
        [data.currentPosition.row]
        [++data.currentPosition.stack]
        =[];
    data.currentPosition.height=-1;
}

function NextRow(){
    data.zones
        [data.currentPosition.zone]
        [++data.currentPosition.row]
        =[[]];
    data.currentPosition.height=-1;
    data.currentPosition.stack=0;
}

function FindItem(itemID){
    //Create an array to store found items
    var found = [];

    //Find all items with matching ID
    Object.keys(data.zones).forEach(zoneName=>{
        data.zones[zoneName].forEach((row,rowI)=>{
            row.forEach((stack, stackI)=>{
                stack.forEach((item,itemI)=>{
                    if(item.substring(0,6) == itemID){
                        found.push({item,position:{
                            zone: zoneName,
                            row: rowI,
                            stack: stackI,
                            item: itemI
                        }});
                    }
                })
            })
        })
    })

    //Sort found array by date
    found.sort((a,b)=>(
        new Date(
            `20${a.item.substring(10,12)}`,  //Assume Year in barcode is 20XX
            a.item.substring(8,10) - 1,      //Javascript date index starts at 0 (for jan)
            a.item.substring(6,8)
        ).getTime() - new Date(
            `20${b.item.substring(10,12)}`,  //Assume Year in barcode is 20XX
            b.item.substring(8,10) - 1,      //Javascript date index starts at 0 (for jan)
            b.item.substring(6,8)  
        ).getTime()
    ));

    //return found items
    return found;
}



//test
SelectZone("TestZone");
ScannedBarcode("12332110092001");
ScannedBarcode("12332112092003");
ScannedBarcode("12332111092002");
ScannedBarcode("12332110092001");
NextStack();
ScannedBarcode("12333110092001");
ScannedBarcode("12333111092002");
ScannedBarcode("12333112092003");
NextRow();
ScannedBarcode("12333110092001");
ScannedBarcode("12333111092002");
ScannedBarcode("12333112092003");

console.log(JSON.stringify(data,null,4));
console.log(JSON.stringify(FindItem("123321"),null,4));

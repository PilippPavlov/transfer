function addDataTable(parentElm,dataList) { 
    //parentElement - Table
    //dataList = [data1,data2,...,dataN]
    //data = {'atribut1':<value1>,'atribut2':<value2>,...,'atributN':<valueN>}
    if((parentElm != undefined) && (dataList != [])){
        var iframe = document.createDocumentFragment();
        for( var i = 0; i < dataList.length; i++) {
            var tableRow = document.createElement('tr');
            for( var key in dataList[i]) {
                var tableh = document.createElement('th');
                if(dataList[i][key] != undefined)
                    tableh.insertAdjacentHTML('beforeEnd',dataList[i][key]);
                else
                    tableh.insertAdjacentHTML('beforeEnd',' ');
                tableRow.appendChild(tableh);
            }
            iframe.appendChild(tableRow);
        }
        parentElm.appendChild(iframe);
    }
};
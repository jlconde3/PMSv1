function create_table(table_type){
    switch(table_type){
        case "projects":
            //Statements
            break;

        case "actions":
            //Statements
            break;
        
        case "wps":
            //Statements
            break;

        case "users":
            //Statements
            break;
        case "users-activity":
            //Statements
            break;
    }
}

function transform_data_table (table_id,response){
    for (let i in response){
        let tr = document.createElement('tr');
        tr.setAttribute('id',i);
        
        for (let j in response[i]){
            let td = document.createElement('td');
            td.innerHTML = response[i][j];
            tr.appendChild(td);
        }
        document.getElementById(table_id).appendChild(tr);
    };
}

function hide_table (){
    const tables = document.getElementsByName('table')
    const tables_array = [...tables]
    document.getElementById('intro-text').style.display = "none"
    tables_array.forEach((item)=>{item.setAttribute('style', 'display:none')})
}
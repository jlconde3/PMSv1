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
    const tables = document.getElementsByName('table');
    const tables_array = [...tables];
    document.getElementById('intro-text').style.display = "none";
    tables_array.forEach((item)=>{item.setAttribute('style', 'display:none')})
}

function delete_list(element_id){
    const list = document.getElementById(element_id);
    while (list.hasChildNodes()){
        list.removeChild(list.firstChild);
    }
}

function add_more(parente_element,content){
    const container = document.getElementById(parente_element);
    let div = document.createElement('div');
    div.setAttribute('class','group');
    div.innerHTML = content;
    container.appendChild(div);
}

function element_id_value(element_id){
    return document.getElementById(element_id).value;
}

function element_name_value(element_name){
    const list_values = [];
    for (let i of document.getElementsByName(element_name)){   
        list_values.push(i.value);
    }
    return list_values;
}


function html_list(response,html_list){
    const container = document.getElementById(html_list);
    for (let i in response){
        var content = document.createElement('option');
        content.value = option;
        container.appendChild(content);
    }
}

function retrive_data(data,url,lists_array){
    fetch(url,{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{'Content-Type': 'application/json'}
    })
    .then((response => response.json()))
    .then( data => {
        for (const list of lists_array){
            let container = document.getElementById(list);
            for (const option of data){
                var content = document.createElement('option');
                content.value = option;
                content.innerHTML = option;
                container.appendChild(content)
            }
        }
    })
};

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
};

function hide_table (){
    const tables = document.getElementsByName('table');
    const tables_array = [...tables];
    document.getElementById('intro-text').style.display = "none";
    tables_array.forEach((item)=>{item.setAttribute('style', 'display:none')})
};

function delete_childs(element_id){
    const list = document.getElementById(element_id);
    while (list.hasChildNodes()){
        list.removeChild(list.firstChild);
    }
}

function delete_value(element_id){
    document.getElementById(element_id).value=null;
};

function add_more(parent_element,content){
    const container = document.getElementById(parent_element);
    let div = document.createElement('div');
    div.setAttribute('class','group');
    div.innerHTML = content;
    container.appendChild(div);
};

function add_validate_window(parent_element, content){
    const container = document.getElementById(parent_element);
    let div = document.createElement('div');
    div.innerHTML = content;
    container.appendChild(div);
};

function element_id_value(element_id){
    input = document.getElementById(element_id)
    if (input.type == "number"){
        return input.value.toUpperCase().replace(',','.');
    }
    return input.value.toUpperCase()
};

function element_name_value(element_name){
    const list_values = [];
    for (let i of document.getElementsByName(element_name)){  
        if (i.type == "number"){
            list_values.push(i.value.toUpperCase().replace(',','.'));
        }
        else{
            list_values.push(i.value.toUpperCase());
        }
    }
    return list_values;
};


function html_list(response,html_list){
    const container = document.getElementById(html_list);
    for (let i in response){
        var content = document.createElement('option');
        content.value = option;
        container.appendChild(content);
    }
};

function retrive_data(reload,data,url,input_id){
    let list = document.getElementById(input_id).nextElementSibling;

    fetch(url,{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{'Content-Type': 'application/json'}
    })
    .then((response => response.json()))
    .then( data => {
        if (reload == true){
            let container =  list
            for (const option of data){
                var content = document.createElement('option');
                content.value = option;
                content.innerHTML = option;
                container.appendChild(content)
            }
        }
    })
    .then(()=> display_select_input(input_id,list.id))
};

function display_select_input(input_id,datalist_id){
    document.getElementById(datalist_id).style.display = 'block';
    var options = [...document.getElementById(datalist_id).options]

    options.forEach((item)=>{
        item.addEventListener('click',()=>{
            document.getElementById(input_id).value = item.value;
            document.getElementById(datalist_id).style.display = 'none';
        },false)
    });

    var currentFocus = -1;
    document.getElementById(input_id).oninput = function() {
        currentFocus = -1;
        var text = document.getElementById(input_id).value.toUpperCase();
        options.forEach((item)=>{
            if(item.value.toUpperCase().indexOf(text) > -1){
                item.style.display = "flex";
            }
            else{
                item.style.display = "none";
            }
        });
    }
    window.addEventListener('click',()=>{
        document.getElementById(datalist_id).style.display = 'none';
    })
};


function loader (){
    const container = document.getElementById('window');
    let dialog = document.createElement('dialog');
    dialog.setAttribute('id','loader_window')
    dialog.innerHTML = `
    <p class = "loading_title">Saving your data in the best possible way. This operation will take some time...</p>
    <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    `;
    container.appendChild(dialog);
    document.getElementById('loader_window').showModal();
};



function retrive_list(parent_element){
    empty_list = []
    for (i of parent_element){
        empty_list.push(i.value);
    }
    return empty_list;
}

function reset_users_wp (j){
    delete_childs('validate_window')
    document.getElementById('validate_window').close();
    for (let u = 1; u<j+1; u++){
        console.log(action_area_task)
        delete action_area_task[`users_${u}`]}
        action_area_task[`users_0`] = true;
    q = 1;
}
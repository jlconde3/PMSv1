
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

function delete_value(id_fields){
    for (i of id_fields){
        document.getElementById(i).value=null;
    }
};


function delete_value_by_name(name_fields){
    for (i of name_fields){
        for (j of document.getElementsByName(i)){
            j.value=null;
        }
    }
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

function retrive_data(data,url,input_id,id_list,name_list){
    let list = document.getElementById(input_id).nextElementSibling;
    delete_childs(list.id)

    fetch(url,{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{'Content-Type': 'application/json'}
    })
    .then((response => response.json()))
    .then((data) => {
        let container =  list
        for (const option of data){
            var content = document.createElement('option');
            content.value = option;
            content.innerHTML = option;
            container.appendChild(content)
        }
    })
    .then(()=> {disabled_fields()})
    .then(()=>{display_select_input(input_id,list.id,id_list,name_list)})
};

function display_select_input(input_id,datalist_id,id_list,name_list){
    document.getElementById(datalist_id).style.display = 'block';
    var options = [...document.getElementById(datalist_id).options]

    options.forEach((item)=>{
        item.addEventListener('click',()=>{
            document.getElementById(input_id).value = item.value;
            document.getElementById(datalist_id).style.display = 'none';
            delete_value(id_list);
            delete_value_by_name(name_list)
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
        delete action_area_task[`users_${u}`]}
        action_area_task[`users_0`] = true;
    q = 1;
}

function area_action(action_id,area_id){
    data = {
        project:document.getElementById('project_code'),
        action_code:document.getElementById(action_id)
    }
    fetch('/tools/action_area',{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then((data) => {document.getElementById(area_id).value = data
    })
}


function disabled_fields(){
    
    if (document.getElementById('wp_line').value == 'DESIGN'){
        for (i of document.getElementsByName('task_area')){
            i.disabled = false;
        }
        for (i of document.getElementsByName('task_action')){
            i.disabled = true;
        }
    }
    else if (document.getElementById('wp_line').value == 'ACTIONS'){
        for (i of document.getElementsByName('task_area')){
            i.disabled = true;
        }
        for (i of document.getElementsByName('task_action')){
            i.disabled = false;
        }
    }
    
}

function retrive_data_actions(data,url,input_id,id_list,name_list){
    let list = document.getElementById(input_id).nextElementSibling;
    delete_childs(list.id)

    fetch(url,{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{'Content-Type': 'application/json'}
    })
    .then((response => response.json()))
    .then((data) => {
        let container =  list
        for (const option of data){
            var content = document.createElement('option');
            content.value = option;
            content.innerHTML = option;
            container.appendChild(content)
        }
    })
    .then(()=>{display_select_input(input_id,list.id,id_list,name_list)})
};

function isEmpty(str) {
    return !str.trim().length;
}

function padTo2Digits(num) {
    return num.toString().padStart(2, '0');
}

function get_date (input){
    const date = new Date(input)
    return [
        date.getFullYear(),
        padTo2Digits(date.getMonth()+1),
        padTo2Digits(date.getDate())
    ].join('-')
}
let j = 1;

document.getElementById('project').addEventListener('click',()=>{
    retrive_data_actions(
        data = {},
        url = '/tools/projects',
        input_id = 'project',
        id_list = [],
        name_list = []
    )
});

document.getElementById('subaction').addEventListener('click',()=>{
    retrive_data_actions(
        data = {project:document.getElementById('project').value,},
        url = '/tools/subactions',
        input_id = 'subaction',
        id_list = [],
        name_list = []
    )
});

document.getElementById('retrive_button').addEventListener('click',()=>{
    const project = document.getElementById('project').value;
    const subaction = document.getElementById('subaction').value;

    if (!isEmpty(subaction)){
        fetch('/actions/retrive_subaction',{
            credentials: 'include',
            method: 'POST',
            body: JSON.stringify({project:project,subaction:subaction}),
            headers:{'Content-Type': 'application/json'}
        })
        .then(response => response.json())
        .then(data => display_data_project(data['response']))
    }
});

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

function display_data_project (response){
    document.getElementById('action').value = response[1];
    document.getElementById('client').value = response[3];
    document.getElementById('custom').value = response[10];
    document.getElementById('phase').value = response[7];
    document.getElementById('discipline').value = response[6];
    document.getElementById('system').value = response[16];
    document.getElementById('type').value = response[4];
    document.getElementById('zone').value = response[11];
    document.getElementById('area').value = response[12];
    document.getElementById('time').value = response[13];
    document.getElementById('description').value = response[8];
}

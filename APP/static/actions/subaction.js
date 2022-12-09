let j = 1;

document.getElementById('project').addEventListener('click',()=>{
    retrive_data_actions(
        data = {},
        url = '/data/projects',
        input_id = 'project',
        id_list = [],
        name_list = []
    )
});

document.getElementById('subaction').addEventListener('click',()=>{
    retrive_data_actions(
        data = {project:document.getElementById('project').value,},
        url = '/data/subactions',
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
    document.getElementById('action').value = response[0];
    document.getElementById('client').value = response[1];
    document.getElementById('custom').value = response[2];
    document.getElementById('zone').value = response[3];
    document.getElementById('area').value = response[4];
    document.getElementById('time').value = response[5];
    document.getElementById('status').value = response[6];
}

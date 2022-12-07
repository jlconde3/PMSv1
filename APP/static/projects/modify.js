document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('code').addEventListener('click',()=>{
    retrive_data_actions(
        data = {},
        url = '/tools/projects',
        input_id = 'code',
        id_list = ['name','client','section','division','budget','margin','default','actions',
        'management','others','work_result','management_result','others_result'],
        name_list = []
    )
});

document.getElementById('retrive_button').addEventListener('click',function retrive_data(){
    const code = document.getElementById('code').value 
    fetch('/projects/retrive_data',{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify({code:code}),
        headers:{'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => display_data_project(data['response']))
});

document.getElementById('reload_button').addEventListener('click',function reload_hours(){
    const budget = document.getElementsByName('budget');
    const margin = document.getElementsByName('margin');
    const cpt = document.getElementsByName('default');
    const management = document.getElementsByName('management');
    const other = document.getElementsByName('others');
    const usefull_hours = budget[0].value*(1-margin[0].value);
    const management_hours = usefull_hours*management[0].value;
    const other_hours = usefull_hours*other[0].value;

    document.getElementById('work_result').value = Math.round((usefull_hours-management_hours-other_hours)/cpt[0].value)
    document.getElementById('management_result').value = Math.round(management_hours/cpt[0].value)
    document.getElementById('others_result').value = Math.round(other_hours/cpt[0].value)

});


function display_data_project (response){
    document.getElementById('name').value = response[3];
    document.getElementById('client').value = response[4];
    document.getElementById('section').value = response[5];
    document.getElementById('division').value = response[6];
    document.getElementById('budget').value = response[7];
    document.getElementById('margin').value = response[8];
    document.getElementById('default').value = response[9];
    document.getElementById('actions').value = response[10];
    document.getElementById('management').value = response[11];
    document.getElementById('others').value = response[12];
    document.getElementById('work_result').value = response[14];
    document.getElementById('management_result').value = response[15];
    document.getElementById('others_result').value = response[16];
}

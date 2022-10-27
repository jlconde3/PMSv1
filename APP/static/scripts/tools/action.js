var reload_projects = true;
var reload_types = true;
var reload_disciplines = true;
var reload_phases = true;
var reload_zones = true;
var reload_areas = true;


document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('project_code').addEventListener('click',()=>{
    retrive_data(
        reload = reload_projects,
        data = {},
        url = '/tools/projects',
        input_id = 'project_code',
        list_id = 'projects',
    )
    reload_projects = false;
})

document.getElementById('project_code').addEventListener('change',()=>{
    delete_list('types');
    delete_value('action_type')
    delete_list('disciplines');
    delete_value('discipline_code')
    delete_list('phases');
    delete_value('phase_code')
    reload_types = true;
});

document.getElementById('action_type').addEventListener('click',()=>{
    retrive_data(
        reload = reload_types,
        data = {},
        url = '/tools/projects',
        input_id = 'action_type',
        list_id = 'types',
    )
    reload_types = false;   
});

document.getElementById('discipline_code').addEventListener('click',()=>{
    retrive_data(
        reload = reload_disciplines,
        data = {},
        url = '/tools/projects',
        input_id = 'discipline_code',
        list_id = 'disciplines',
    )
    reload_disciplines = false;   
});

document.getElementById('phase_code').addEventListener('click',()=>{
    retrive_data(
        reload = reload_phases,
        data = {},
        url = '/tools/projects',
        input_id = 'phase_code',
        list_id = 'phases',
    )
    reload_phase = false;   
});



//Template for actions
let action_template = `
<div>
    <label class = "label-title">Subaction</label>
</div>
<div class="fields-group">
    <div>
        <label class = "label-field">Custom code</label><br>
        <input class = "input-4" type="text" name = "custom_code">
    </div>
    <div class="dropdwn">
        <label class = "label-field">Zone</label><br>
        <input class = "input-4" type="text" name = "subaction_zone">
        <datalist id="zones"></datalist>
    </div>
    <div class="dropdwn">
        <label class = "label-field">Area</label><br>
        <input class = "input-4" type="text" name = "subaction_area">
        <datalist id="areas"></datalist>
    </div>
    <div>
        <label class = "label-field">Time</label><br>
        <input class = "input-4" type="number" id = "subaction_time">
    </div>
</div>
`

document.getElementById('more_button').addEventListener('click',() => {
    add_more('subactions',action_template);
});
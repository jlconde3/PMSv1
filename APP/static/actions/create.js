let j = 1;

document.getElementById('project').addEventListener('click',()=>{
    retrive_data_actions(
        data = {},
        url = '/data/projects',
        input_id = 'project',
        id_list = ['phase','discipline','system','type'],
        name_list = ['zone','area','time']
    )
});

document.getElementById('phase').addEventListener('click',()=>{
    retrive_data_actions(
        data = {project:document.getElementById('project').value},
        url = '/data/phases',
        input_id = 'phase',
        id_list = ['discipline','system','type'],
        name_list = ['zone','area','time']
    )
});

document.getElementById('discipline').addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            project:document.getElementById('project').value,
        },
        url = '/data/disciplines',
        input_id = 'discipline',
        id_list = ['system','type'],
        name_list = ['zone','area','time']
    )
});

document.getElementById('system').addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            project:document.getElementById('project').value,
            discipline:document.getElementById('discipline').value
        },
        url = '/data/systems',
        input_id = 'system',
        id_list = [],
        name_list = ['zone','area','time']
    )
});

document.getElementById('type').addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            project:document.getElementById('project').value,
        },
        url = '/data/stations',
        input_id = 'type',
        id_list = [],
        name_list = []
    )
});


document.getElementById('zone_0').addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            project:document.getElementById('project').value,
            discipline:document.getElementById('discipline').value,
            system:document.getElementById('system').value
        },
        url = '/data/zones',
        input_id = 'zone_0',
        id_list = [],
        name_list = []
    )
});

document.getElementById('area_0').addEventListener('click',()=>{
    retrive_data_actions(
        data = {
            project:document.getElementById('project').value,
            discipline:document.getElementById('discipline').value,
            system:document.getElementById('system').value,
            zone:document.getElementById('zone_0').value
        },
        url = '/data/areas',
        input_id = 'area_0',
        id_list = [],
        name_list = []
    )
});


document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('more_button').addEventListener('click',() => {
    let i = j;
    add_more('subactions',
    `
    <div>
        <label class = "label-title">Subaction</label>
    </div>
    <div class="fields-group">
        <div>
            <label class = "label-field">Custom code</label><br>
            <input name="custom" class = "input-4" type="text">
        </div>
        <div class="dropdwn">
            <label class = "label-field">Zone</label><br>
            <input name = "subaction_zone" class = "input-4" type="text"  id = "zone_${j}">
            <datalist id="zones_${j}" class = "input-4"></datalist>
        </div>
        <div class="dropdwn">
            <label class = "label-field">Area</label><br> 
            <input name="subaction_area" id = "area_${j}" class = "input-4" type="text">
            <datalist id="areas_${j}" class = "input-4" ></datalist>
        </div>
        <div>
            <label class = "label-field">Time</label><br>
            <input name = "subaction_time" class = "input-4" type="number">
        </div>
    </div>
    `);

    document.getElementById(`zone_${i}`).addEventListener('click',()=>{
        retrive_data_actions(
            data = {
                project:document.getElementById('project').value,
                discipline:document.getElementById('discipline').value,
                system:document.getElementById('system').value,
            },
            url = '/data/zones',
            input_id = `zone_${i}`,
            id_list = [],
            name_list = []
        )
    })

    document.getElementById(`area_${i}`).addEventListener('click',()=>{
        retrive_data_actions(
            data = {
                project:document.getElementById('project').value,
                discipline:document.getElementById('discipline').value,
                system:document.getElementById('system').value,
                zone:document.getElementById(`zone_${i}`).value
            },
            url = '/data/areas',
            input_id = `area_${i}`,
            id_list = [],
            name_list = []
        )
    })
    j++;
});

document.getElementById('description').addEventListener('keyup',()=>{
    var characterCount = document.getElementById('description').value.length;
    current = document.getElementById('current');
    current.innerText = characterCount;

});
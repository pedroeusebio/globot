$(document).ready(function() {
  $('.alert-success').hide();
  $('.alert-danger').hide();
});

$("#createPoll").submit(function(e) {
  e.preventDefault();
  var payload = submitPoll(this);
  console.log(payload);
  $('.alert-success').show();
  $('.alert-danger').hide();

  // $.post('asdasd', payload)
  //   .done(function(data) {
  //     // verify success
  //           //verify error
  //     $('.alert-danger').alert();
  //     $('.alert-success').alert('close');
  //   });

});

function submitPoll(p) {
  var poll = $(p);
  var serial = poll.serializeArray();
  var obj = {option: []};
  serial.map(function(e) {
    if (e.name == 'option'){
      obj.option.push(e.value);
    } else {
      obj[e.name] = e.value;
    }
  });
  return obj;
}

$('#addOption').on('click', function() {
  var numOption = $('.input-group').length;
  var $option = $(`<div class="col-sm-8 input-group"><span class="input-group-addon">Opcao ${numOption}</span><input type="text" class="form-control" placeholder="opcao" aria-describedby="sizing-addon2" name="option"></div>`);
  $('#div-options').append($option);
});

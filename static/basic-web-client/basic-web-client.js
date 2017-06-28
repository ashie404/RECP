
function update() {

  $.getJSON('recp/api/v1.0/message' , function(data) {
    var tbl_body = "";
    var odd_even = false;
    console.log(data);
    $.each(data, function() {
        var tbl_row = "";
        var delbutton = "<td><button onclick='deletemsg("
        var delbutton2 = ")'>Delete</button>";
        var editbtn = "<button onclick='editmsg("
        var editbtn2 = ")'>Edit</button></td>"
        $.each(this, function(k , v) {
            tbl_row += "<tr><td>User" + v.authorid + ": " +v.content+"</td><td>Message ID: " + v.id + ", Edited: " + v.edited + "</td>" + delbutton + v.id + delbutton2 + editbtn + v.id + editbtn2 + "</tr>";
        })
        tbl_body += "<tr><td><b>Message</b></td><td><b>Message Information</b></td><td><b>Actions</b></td></tr><tr>"+tbl_row+"</tr>";
        odd_even = !odd_even;
    })
    $("#chat").html(tbl_body);
});

  //$("#chat").html("<tr><td><center><b>Failed to connect to update chat logs.</b></center></td></tr>");

}

function submit() {
  $.ajax({
    type: 'POST',
    url: 'recp/api/v1.0/message',
    data: '{"authorid":1,"content":"' + $('#chatbox').val() + '"}',
    contentType: "application/json",
    dataType: 'json'
  });
  update();
}

function deletemsg(id) {
  $.ajax({
    type: 'DELETE',
    url: 'recp/api/v1.0/message/' + id
  });
  update();
}

function editmsg(id) {
  var msg = prompt('What to replace the message with?');

  if (msg == "")
  {
    alert('You must enter a string to replace it with!');
  }
  else if (msg == null) {
    alert('User cancelled message editing.')
  }
  else {
    $.ajax({
      type: 'PUT',
      url: 'recp/api/v1.0/message/' + id,
      data: '{"content":"' + msg + '"}',
      contentType: "application/json",
      dataType: 'json'
    });
    update();
  }
}

window.onerror = function(msg, url, linenumber) {
    alert('Error message: '+msg+'\nURL: '+url+'\nLine Number: '+linenumber);
    return true;
}

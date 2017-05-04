
function update() {
  $.getJSON('http://localhost:5000/recs/api/v1.0/message' , function(data) {
    var tbl_body = "";
    var odd_even = false;
    console.log(data);
    $.each(data, function() {
        var tbl_row = "";
        $.each(this, function(k , v) {
            tbl_row += "<tr><td>User" + v.authorid + ": " +v.content+"</td><td>Message ID: " + v.id + "</td></tr>";
        })
        tbl_body += "<tr class=\""+( odd_even ? "odd" : "even")+"\">"+tbl_row+"</tr>";
        odd_even = !odd_even;
    })
    $("#chat").html(tbl_body);
});
}

function submit() {
  $.ajax({
    type: 'POST',
    url: 'http://localhost:5000/recs/api/v1.0/message',
    data: '{"authorid":1,"content":"' + $('#chatbox').val() + '"}',
    success: function(data) { alert('data: ' + data); },
    contentType: "application/json",
    dataType: 'json'
  });
}

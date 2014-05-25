function printdiv(val)
{
	var headstr = "<html><head><title></title></head><body>";
	var footstr = "</body>";
	var newstr = $('#'+val)[0].innerHTML;
	var oldstr = document.body.innerHTML;
	document.body.innerHTML = headstr+newstr+footstr;
	window.print();
	document.body.innerHTML = oldstr;
	return false;
}

now = new Date();
day = new Object();
month = new Object();


day[0] = "Sunday";
day[1] = "Monday";
day[2] = "Tuesday";
day[3] = "Wednesday";
day[4] = "Thursday";
day[5] = "Friday";
day[6] = "Saturday";

month[0] = "January";
month[1] = "February";
month[2] = "March";
month[3] = "April";
month[4] = "May";
month[5] = "June";
month[6] = "July";
month[7] = "August";
month[8] = "September";
month[9] = "October";
month[10] = "November";
month[11] = "December";


year = now.getYear();

if (year < 1000) year += 1900

document.write("<br>" + day[now.getDay()] + ", " + month[now.getMonth()] + " " + now.getDate() + ", " + year);

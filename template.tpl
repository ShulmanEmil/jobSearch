<!DOCTYPE html>
<html lang="ru" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <p>The open wish items are as follows:</p>
<table border="1">
%for r in rows:
  <tr>
    %n = 0
    %i = 4
  %for c in r:
  %n += 1
  %while i == n:
    %n += 3
    <td><a href="{{c}}">Подробнее...</a></td>
    %break
    %else:
    <td>{{c}}</td>
  %end
  %end
  </tr>
%end
</table>

<form class="" action="/add_vacancies_list" method="get">
  <select name="add_vacancies">
    %for c in vaca:
    <option>{{c}}</option>
    %end
  </select>
  <select name="add_company">
    %for c in com:
    <option>{{c}}</option>
    %end
  </select>
  <select name="add_branch">
    %for c in bra:
    <option>{{c}}</option>
    %end
  </select>
  <input type="number" name="salary"
       min="1">
  <textarea name="desc" cols="40" rows="3"></textarea>
  <input type="submit" name="save_vacancies_list" value="Отправить">
</form>

<form class="" action="/add_vacancies" method="get">
  <input type="text" name="vacancies" value="">
  <input type="submit" name="save_vacancies" value="Отправить">
</form>

<form class="" action="/add_company" method="get">
  <input type="text" name="company" value="">
  <input type="submit" name="save_company" value="Отправить">
</form>



  </body>
</html>

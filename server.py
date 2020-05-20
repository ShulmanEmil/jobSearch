from bottle import route, template, run, static_file, redirect, request
import pymysql, codecs

con = pymysql.connect('localhost', 'non-root', '*', 'job_search')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,
                       root='/home/shulman/Desktop/job_search/static')

@route('/')
def list():

    with con:
        cur = con.cursor()
        cur.execute("SELECT vacancies.name, company.name, branch.name, vacancies_list.id FROM vacancies_list INNER JOIN vacancies ON vacancies_list.vacancies_id = vacancies.id INNER JOIN company ON vacancies_list.company_id = company.id INNER JOIN branch ON vacancies_list.branch_id = branch.id")
        result = cur.fetchall()
        #Сделать запрос где будут все
        def pick(choiceNumber):
            pickList = []
            for row in result:
                pickList.append(row[choiceNumber])
            return pickList
        vacan = pick(0)
        comp = pick(1)
        bran = pick(2)
        # cur.execute("SELECT name FROM vacancies")
        # vacan = cur.fetchall()
        # cur.execute("SELECT name FROM company")
        # comp = cur.fetchall()
        # cur.execute("SELECT name FROM branch")
        # bran = cur.fetchall()
        return template('template', rows=result, vaca=vacan, com=comp, bra=bran)

@route('/<id:int>') #Полный ввывод вакансии
def callback(id):
    assert isinstance(id, int)
    cur = con.cursor()
    cur.execute("SELECT vacancies.name, company.name, branch.name, vacancies_list.salary FROM vacancies_list INNER JOIN vacancies ON vacancies_list.vacancies_id = vacancies.id INNER JOIN company ON vacancies_list.company_id = company.id INNER JOIN branch ON vacancies_list.branch_id = branch.id WHERE vacancies_list.id = %s", (id))
    detail = cur.fetchall()
    def conc(choiceNumber):
        concList = []
        for row in detail:
            concList.append(row[choiceNumber])
        for i in concList:
            concList = i
        return concList
    return  template('detail', r=conc(0), c=conc(1), branch=conc(2) ,salary=conc(3))

@route('/add_vacancies_list', method='GET')
def add_vacancies_list():
    if request.GET.get('save_vacancies_list','').strip():

        vacancies = request.GET.get('add_vacancies', '').strip()
        vacancies = bytes(vacancies,'iso-8859-1').decode('utf-8')

        company = request.GET.get('add_company', '').strip()
        company = bytes(company,'iso-8859-1').decode('utf-8')

        branch = request.GET.get('add_branch', '').strip()
        branch = bytes(branch,'iso-8859-1').decode('utf-8')

        salary = request.GET.get('salary', '').strip()
        description = request.GET.get('desc', '').strip()

        return '<p>Успешно добавленно %s</p>' %salary
    else:
        return '<p>Что-то пошло не так</p>'

@route('/add_vacancies', method='GET')
def add_vacancies():
    if request.GET.get('save_vacancies','').strip():

        vacancies = request.GET.get('vacancies', '').strip()

        with con:
            cur = con.cursor()
            sql = "INSERT INTO vacancies(name)"\
            +"VALUES (%s)"
            cur.execute(sql,(vacancies))
            con.commit()

        return '<p>Успешно добавленно %s</p>' %vacancies

    else:
        return '<p>Что-то пошло не так</p>'


@route('/add_company', method='GET')
def add_company():
    if request.GET.get('save_company','').strip():

        company = request.GET.get('company', '').strip()

        with con:
            cur = con.cursor()
            sql = "INSERT INTO company(name)"\
            +"VALUES (%s)"
            cur.execute(sql,(company))
            con.commit()

        return '<p>Успешно добавленно %s</p>' %company

    else:
        return '<p>Что-то пошло не так</p>'


run(host='localhost', port=8082, debug=True)

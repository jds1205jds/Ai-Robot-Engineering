CREATE TABLE employees (
    dept TEXT,
    job TEXT,
    salary INTEGER
);

INSERT INTO employees VALUES
('개발','백엔드',6000),
('개발','백엔드',6500),
('개발','프론트',5500),
('개발','프론트',5200),
('영업','영업사원',4000),
('영업','영업사원',4200),
('영업','팀장',7000),
('인사','인사담당',4500),
('인사','팀장',6000),
('인사','팀장',6200);

-- 급여가 5천이상인 사람들의 부서별 평균급여 구하기
SELECT dept, ROUND(AVG(salary),2)
FROM employees
GROUP BY dept
HAVING AVG(salary) >=5000;

-- 직원이 4명 이상인 부서 구하기
SELECT dept, count(*) 
FROM employees
GROUP BY dept
HAVING count(*) > 3
;

-- 직무별 평균 급여가 6000 이상인 직무 구하기
SELECT job, AVG(salary) 
FROM employees
GROUP BY job
HAVING AVG(salary) >= 6000
;

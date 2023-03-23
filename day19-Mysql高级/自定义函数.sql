-- 创建函数
-- SET GLOBAL log_bin_trust_function_creators=TRUE;
-- CREATE FUNCTION hello_fun() RETURNS VARCHAR(20)
-- BEGIN
-- RETURN 'hello sql';
-- END


-- SHOW FUNCTION STATUS;

-- SELECT hello_fun()

-- delimiter %%
-- DROP FUNCTION if EXISTS hello_say%%
-- CREATE FUNCTION hello_say(uname VARCHAR(10)) RETURNS VARCHAR(20)
-- BEGIN
-- RETURN CONCAT('hello--',uname);
-- END
-- %%
-- delimiter;

-- SELECT hello_say('刘德华');
-- SELECT hello_say(name) from student;


-- delimiter //
-- DROP FUNCTION if EXISTS total_count//
-- CREATE FUNCTION total_record() RETURNS VARCHAR(20)
-- BEGIN
-- DECLARE total_count int DEFAULT 0;
-- SELECT count(1) FROM student INTO total_count;
-- RETURN CONCAT('学生表中的数据记录数量是：',total_count);
-- END
-- //
-- delimiter;
-- 
-- SELECT total_record();

-- delimiter //
-- DROP FUNCTION if EXISTS total_record_var//
-- CREATE FUNCTION total_record_var() RETURNS VARCHAR(50)
-- BEGIN
-- DECLARE total_count int DEFAULT 0;
-- SELECT count(1) FROM student INTO @total_count_student;
-- SELECT count(1) FROM course INTO @total_count_course;
-- RETURN CONCAT('学生表中的数据记录数量是：',@total_count_student,' , ','课程表中的数据记录量是：',@total_count_course);
-- END
-- //
-- delimiter;

-- SELECT total_record_var();


-- delimiter //
-- DROP FUNCTION if EXISTS fun_if//
-- CREATE FUNCTION fun_if(age int) RETURNS VARCHAR(50)
-- BEGIN
-- if age<20 THEN SET @msg='嘿 你还不到20岁';
-- else SET @msg='你已经超过20岁，可以参军报效祖国了';
-- end if;
-- RETURN @msg;
-- END
-- //
-- delimiter;

SELECT fun_if(20);
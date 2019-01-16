*/Vers 1
Select * 
from students 
where ((quality1='evil' and quality2='cunning')
or (quality1='brave' and quality2 !='evil')
or  (quality1='studious' or quality2='intelligent')
or (quality1='hufflepuff' or quality2='hufflepuff'))
order by id


*/Vers 2
select id, name, quality1 as q1, quality2 as q2,
	case when q1 = 'brave' and q2 != 'evil' then 'Gryffindor'
		 when q1 = 'evil' and q2 = 'cunning' then 'Slytherin'	
		 when q1 = 'studious' or q2 = 'intelligent' then 'Ravenclaw'
		 when q1 = 'hufflepuf' or q2 = 'hufflepuf' then 'Hufflepuf'
	end as 'Faculty'
from students	
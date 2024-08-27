

SELECT w2.id
FROM Weather w1, Weather w2
where datediff(w2.recordDate,w1.recordDate)=1  and w2.temperature>w1.temperature;
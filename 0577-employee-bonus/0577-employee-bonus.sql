select name, bonus
from Employee left join bonus on Employee.empId=Bonus.empId
where bonus<1000 or bonus is null
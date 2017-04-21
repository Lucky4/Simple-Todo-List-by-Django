    $('#myModal').modal({
      keyboard: false
    })

    window.onload = function() {
      // 获取三个form-group元素
      var formGroup = document.getElementsByClassName("form-group");

      // 设置todo节点初始值
      var todo = document.getElementById("hidden-todo").getAttribute("name");
      formGroup[0].childNodes[3].value = todo;

      // 设置priority节点初始值
      var priority = document.getElementById("hidden-priority").getAttribute("name");
      var radioWrapper = document.getElementsByClassName("radio");
      for(var key in radioWrapper) {
      	if(radioWrapper[key].childNodes[1].childNodes[1].getAttribute("value") == priority) {
      	  radioWrapper[key].childNodes[1].childNodes[1].setAttribute("checked", "true");
      	  break;
      	}
      }

      // 设置expire_time节点初始值
      var expire_time = document.getElementById("hidden-expire").getAttribute("name");
      formGroup[2].childNodes[3].value = expire_time;
    }

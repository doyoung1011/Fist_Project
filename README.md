# Fist_Project
나의 첫번쨰 프로젝트 저장소


  let seat_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; // 좌석 번호
    let reservation = []; // 예약 좌석
    let menu = 0
    let seat = 0;


    while (menu != 4) {
      menu = Number
        (prompt
          (`1: 예약 2:모든 좌석 현황 3:잔여 좌석 4: 종료`)
        );
      // console.log(menu);

      if (menu == 1) {
        let flag = false; //아직 중복자를 못찾았다는 설정
        seat = Number(prompt("(좌석 번호: 1~10까지 입력"));
     

        for (let j = 0;  j < reservation.length;  j++) {

          if (seat == reservation[j]) //중복값이 입력된 상황
          {
            console.log(`이미 예약된 자리입니다`);
            flag = true;
            break;

            // console.log('중복값 입려됨')
          }
        }
        if (flag == false) {
          reservation.push(seat);
          // console.log(`예약된 자리는 ${seat}입니다`);
          //
        }
      }
     else if (menu == 2) {
        for (let i = 0;  i < seat_num.length;  i++) {
          let flag = false

          for (let k = 0;  k < reservation.length;  k++) {
            if (seat_num[i] == reservation[k]) { //예약 여부 확인

              flag = true
              break

            }

          } if (flag) {
            console.log(`예약 좌석: ${seat_num[i]}번 좌석`)
          }
          else {
            console.log(`남은 좌석: ${seat_num[i]}번 좌석`)
          }
        }

      }
      else if (menu == 3) {
        // console.log(` 잔여좌석 출력 `)



      }
    }

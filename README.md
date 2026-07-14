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
------------------------------------------------


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

// console.log("------------5번 문제----------------");
    // function emailCheck(check) {
    //   //함수로 만들어보자
    //   let pos = check.split("@");
    //   console.log(pos); // 확인용 코드
    //   // console.log(pos[0].slice(0,2))-> 확인용 코드 su 추출용
    //   let mask = "";
    //   for (let i = 0; i < (pos[0].length) - 2; i++) {
    //     mask += "*";

    //   } // for문은 sutdy.todair의 길이만큼만 돌음 
    //   //  우리가 출력할건 to****@naver.com 그럼 시작 조건을  바꾸면 될거같음
    //   console.log(pos[0].slice(0, 2) + mask + '@' + pos[1])


    //   //
    //   // pos[0] 여기에 study.todair가 저장되어있고, 이걸 가리면 됨


    // } emailCheck("sutdy.todair@gmail.com");


    //  이메일을 @기준으로 1/2 내서 앞에 부분만 마스킹
    //  let pos = pos.split("@") -> 이렇게 하면 될거같음


    // emailCheck("sutdy.todair@gmail.com");





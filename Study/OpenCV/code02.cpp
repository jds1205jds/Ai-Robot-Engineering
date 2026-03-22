#include <opencv2/opencv.hpp>  
//시스템에서 먼저 ↑
//#include "opencv2 / opencv.hpp" → 자신의 디렉토리에서 먼저

//웹캠 사용 
void show10()
{
	cv::VideoCapture capture(0);          //생성자호출, 변수0=카메라갯수 디폴트 초기화값
	if (!capture.isOpened())
	{
		std::cout << "카메라가 없음" << std::endl;
		return;
	}
	std::cout << "Web Cam Height : " << cvRound(capture.get(cv::CAP_PROP_FRAME_HEIGHT)) << std::endl;
	std::cout << "Web Cam Width : " << cvRound(capture.get(cv::CAP_PROP_FRAME_WIDTH)) << std::endl;
	//cvrount 소수값이 나오면 반올림해서 정수로 바꿔줌
	cv::Mat screen;
	while (true)
	{
		capture >> screen;
		if (screen.empty())
		{
			std::cerr << "프레임이 들어오지않음" << std::endl;
			break;
		}
		cv::imshow("Web Cam", ~screen);
		cv::imshow("Web Cam2", screen);
		if (cv::waitKey(10) == 27)  break;   //27은 esc를 누르면 무한루프를 종료한다는 뜻

	}
	capture.release();
	cv::destroyAllWindows();
}

//영상 출력 및 반전효과 적용 영상 동시 출력
void show11()
{
	cv::VideoCapture capture("vtest.avi");
	if (!capture.isOpened())
	{
		std::cout << "해당 동영상이 없음" << std::endl;
		return;
	}

	std::cout << "Movie Height : " << cvRound(capture.get(cv::CAP_PROP_FRAME_HEIGHT)) << std::endl;
	std::cout << "Movie Width : " << cvRound(capture.get(cv::CAP_PROP_FRAME_WIDTH)) << std::endl;
	std::cout << "Movie Frame Fps : " << cvRound(capture.get(cv::CAP_PROP_FPS)) << std::endl;

	cv::Mat screen;
	cv::Mat inverse_screen;

	while (true)
	{
		capture >> screen;
		if (screen.empty())
		{
			std::cerr << "프레임이 들어오지않음" << std::endl;
			break;
		}
		inverse_screen = ~screen;
		cv::imshow("Web Cam", screen);
		cv::imshow("inverse_Movie", inverse_screen);
		if (cv::waitKey(100) == 27)  break;   //27은 esc를 누르면 무한루프를 종료한다는 뜻
	
	}
	capture.release();
	cv::destroyAllWindows();
}

//영상출력 및 저장
void show12()
{
	cv::VideoCapture cap(0);    //생성자호출
	if (!cap.isOpened())
	{
		std::cout << "웹캠이 없음" << std::endl;
		return;
	}
	int width = cvRound(cap.get(cv::CAP_PROP_FRAME_WIDTH));
	int height = cvRound(cap.get(cv::CAP_PROP_FRAME_HEIGHT));
	double fps = cap.get(cv::CAP_PROP_FPS); 
	//int fps = cvRound(cap.get(cv::CAP_PROP_FPS));  -> 정수로표현하고싶으면
	//코덱을 선택
	//int width = cvRound(cv::CAP_PROP_FRAME_WIDTH);
	int fourcc = cv::VideoWriter::fourcc('D', 'I', 'V', 'X');
	int delay = cvRound(1000 / fps);
	cv::VideoWriter outputVideo("output.avi", fourcc, fps, cv::Size(width, height));
	
	cv::Mat screen;
	while (true)
	{
		cap >> screen;
		outputVideo << screen;
		cv::imshow("VIDEO", screen);
		if (cv::waitKey(1)== 27) break;
	}
	cap.release();
	cv::destroyAllWindows();
}

//선,화살표,마커
void show13()
{
	cv::Mat canvas(600,600, CV_8UC3, cv::Scalar(255,255,255));
	//선그리기
	cv::line(canvas, cv::Point(50,50),cv::Point(200,50), cv::Scalar(0,0,255),2 ); //두꼐가 2
	//화살표그리기
	cv::arrowedLine(canvas, cv::Point(50, 200), cv::Point(150, 200), cv::Scalar(0, 255, 0), 2);
	//마커그리기
	cv::drawMarker(canvas, cv::Point(30, 350), cv::Scalar(255, 0, 0));
	cv::imshow("CANVAS", canvas);
	cv::waitKey(0);
	cv::destroyAllWindows();
}

//별그리기
void show13_1()
{
	cv::Mat canvas(600, 600, CV_8UC3, cv::Scalar(0, 255, 255));
	cv::line(canvas, cv::Point(300, 50), cv::Point(150, 400), cv::Scalar(0 ,0,0), 4);
	cv::line(canvas, cv::Point(300, 50), cv::Point(450, 400), cv::Scalar(0, 0, 0), 4);
	cv::line(canvas, cv::Point(100,170), cv::Point(450, 400), cv::Scalar(0, 0, 0), 4);
	cv::line(canvas, cv::Point(500, 170), cv::Point(150, 400), cv::Scalar(0, 0, 0), 4);
	cv::line(canvas, cv::Point(100, 170), cv::Point(500, 170), cv::Scalar(0, 0, 0), 4);
	cv::imshow("CANVAS", canvas);
	cv::waitKey(0);
	cv::destroyAllWindows();
}

//캔버스에 글자, 도형그리기
void show14()
{
	cv::Mat canvas(600, 600, CV_8UC3, cv::Scalar(255, 255, 255));
	cv::circle(canvas, cv::Point(250, 250), 60, cv::Scalar(255, 0, 0));
	std::vector<cv::Point>points;
	points.push_back(cv::Point(250, 250));
	points.push_back(cv::Point(300, 250));
	points.push_back(cv::Point(300, 300));
	points.push_back(cv::Point(350, 300));
	points.push_back(cv::Point(350, 350));
	points.push_back(cv::Point(250, 350));
	cv::polylines(canvas, points, true, cv::Scalar(0, 255, 0), 3);
	
	cv::putText(canvas, "I LOVE YOU", cv::Point(50, 100), cv::FONT_ITALIC, 2.0, cv::Scalar(0, 0, 255));
	cv::imshow("CANVAS", canvas);
	cv::waitKey(0);
	cv::destroyAllWindows();
}

//키보드이벤트처리
void show15()
{
	cv::Mat img = cv::imread("lenna.png");
	cv::imshow("Lenna", img);
	while (true)
	{
		//키보드이벤트처리
		int key_value = cv::waitKey(0);
		std::cout << "Input key is " << key_value << std::endl;
		if (key_value == 'i' or key_value == 'I')
		{
			img = ~img;
			cv::imshow("INV_Lenna", img);
		}
		else if (key_value == 'q' or key_value == 27)
		{
			std::cout << "종료" << std::endl;
			break;
		}
	}
}


//이미지에 선그리기 (마우스이벤트처리)
static cv::Point old_pt;
static cv::Mat img;
void on_mouse(int mouse_event, int mouse_x, int mouse_y, int flag, void*)
{
	//std::cout << "마우스클릭" << std::endl;
	switch (mouse_event)
	{
	case cv::EVENT_LBUTTONDOWN:
		std::cout << "왼쪽 클릭" << std::endl;
		old_pt = cv::Point(mouse_x, mouse_y);
		break;
	case cv::EVENT_LBUTTONUP:
		std::cout << "왼쪽 버튼 놓음" << std::endl;
		break;
	case cv::EVENT_MOUSEMOVE:
		std::cout << "마우스가 움직일때" << std::endl;
		if (flag & cv::EVENT_FLAG_LBUTTON)
		{
			cv::line(img, old_pt, cv::Point(mouse_x, mouse_y), cv::Scalar(0, 255, 255), 2);
			cv::imshow("lenna", img);
			old_pt = cv::Point(mouse_x, mouse_y);
		}
		break;
	}
}
void show16()
{
	img = cv::imread("lenna.png");
	if (img.empty()) return;

	cv::namedWindow("lenna");
	cv::setMouseCallback("lenna", on_mouse);
	cv::imshow("lenna", img);
	cv::waitKey(0);
	cv::destroyAllWindows();
}

void on_level_changed(int position, void* userdata)
{
	//cv::Mat img = *(cv::Mat*)userdata;   //형변환
	cv::Mat img = *(static_cast<cv::Mat*>(userdata));  //권장하는 스타일
	img.setTo(position * 16); //바를 움직일때마다 16씩 증가
	cv::imshow("CANVAS", img);
}
void show17()
{
	cv::Mat canvas(800, 800, CV_8UC1);  //c1 컬러하나 색깔 안씀 == 그레이
	cv::namedWindow("CANVASE");
	cv::createTrackbar("Level", "CANVASE", 0, 16, on_level_changed, (void*)&canvas);
	cv::waitKey();
	cv::destroyAllWindows();
 }

void show18()
{
	//마스크연산
	cv::Mat src = cv::imread("lenna.png");
	cv::Mat mask = cv::imread("mask_smile.bmp");
	src.setTo(cv::Scalar(0, 255, 0));
	cv::imshow("LENNA", src);
	cv::imshow("MASK", mask);
	cv::waitKey();
	cv::destroyAllWindows();
}

void show19()
{
	cv::Mat src = cv::imread("airplane.bmp");
	cv::Mat mask = cv::imread("mask_plane.bmp");
	cv::Mat dst = cv::imread("field.bmp");

	cv::Scalar total_pixel = cv::sum(src)(0);

	cv::imshow("DST", dst);
	src.copyTo(dst, mask);
	cv::imshow("Original", src);
	cv::imshow("MASK", mask);
	cv::imshow("Destination", dst);
	cv::waitKey();
	cv::destroyAllWindows();
}
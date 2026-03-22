#include "opencv2/opencv.hpp"

void show1()
{
	//사진출력
	cv::Mat image1 = cv::imread("dog.jpg");
	cv::Mat image2 = cv::imread("dog2.jpg");
	cv::Mat image3;

	if (image1.empty() or image2.empty())
	{
		std::cerr << "파일들이 없습니다" << "\n";
		return;
	}

    //복사(클론)
	image3 = image2.clone();

	std::cout << "1번은  차원 : " << image1.dims << "\n";
	std::cout << "1번은  열 : " << image1.cols << "\n";
	std::cout << "1번은  행 : " << image1.rows << "\n";
	std::cout << "\n";
	std::cout << "2번은  차원 : " << image2.dims << "\n";
	std::cout << "2번은  열 : " << image2.cols << "\n";
	std::cout << "2번은  행 : " << image2.rows << "\n";
	std::cout << "\n";
	std::cout << "3번은  차원 : " << image3.dims << "\n";
	std::cout << "3번은  열 : " << image3.cols << "\n";
	std::cout << "3번은  행 : " << image3.rows << "\n";
	std::cout << "\n";

	cv::namedWindow("dog");
	cv::imshow("dog", image1);
	cv::waitKey(3000);

	cv::namedWindow("dog2");
	cv::imshow("dog2", image2);
	cv::waitKey(3000);

	cv::namedWindow("dog2(copy)");
	cv::imshow("dog2(copy)", image3);
	cv::waitKey(5000);

	cv::destroyAllWindows();
	return;
}

void show2()
{
	//색변화
	cv::namedWindow("Color");
	for(int i = 255; i > 0; i--)
	{
		cv::Mat image(512, 512, CV_8UC3, cv::Scalar(i, 0, 0));
		cv::imshow("Color", image);
		cv::waitKey(10);
	}
	//cv::Mat image2(cv::Size(512,512), CV_8UC1);
	//cv::imshow("Color", image2z
	//cv::waitKey(0);
	cv::destroyAllWindows();


}

void show3()
{
	// zeros(),ones(),eye()
	cv::Mat img1 = cv::Mat::zeros(512, 512, CV_8UC1);
	cv::Mat img2 = cv::Mat::ones(512, 512, CV_8UC1);
	cv::Mat img3 = cv::Mat::eye(512, 512, CV_8UC1)*255;
	cv::namedWindow("Window");
	cv::imshow("Window", img1);
	cv::namedWindow("Window2");
	cv::imshow("Window2", img2);
	cv::namedWindow("Window3");
	cv::imshow("Window3", img3);
	cv::waitKey();
	cv::destroyAllWindows();
}

void show4()
{
	//복사
	cv::Mat img1 = cv::imread("dog2.jpg");
	if (img1.empty())
	{
		std::cerr << "파일없음" << std::endl;
		return;
	}

	//복사하는 3가지 방법
	cv::Mat img2 = img1.clone();
	cv::Mat img3;   //임시 저장 MATRIX
	img2.copyTo(img3);
	cv::Mat img4 = img1;  //복사생성자(copy constructor), 얕은 복사(shallow copy)

	//img1.setTo(cv::Scalar(0, 255, 255));

	cv::namedWindow("DOG");
	cv::imshow("DOG", img1);
	cv::namedWindow("Clone_DOG");
	cv::imshow("Clone_DOG", img2);
	cv::namedWindow("Copy_DOG");
	cv::imshow("Copy_DOG", img3);
	cv::namedWindow("4_DOG");
	cv::imshow("4_DOG", img4);

	cv::waitKey();
	cv::destroyAllWindows();
}

void show5()
{	
	//이미지반전
	cv::Mat img1 = cv::imread("cat.bmp");
	if (img1.empty())
	{
		std::cerr << "파일없음" << std::endl;
		return;
	}
	cv::Mat img2 = ~img1;
	cv::Mat img3 = img1(cv::Rect(220, 120, 340, 240));   //Rect 클래스

	cv::namedWindow("CAT");
	cv::imshow("CAT", img1);
	cv::namedWindow("NOT_CAT");
	cv::imshow("NOT_CAT", img2);
	cv::namedWindow("CUT_CAT");
	cv::imshow("CUT_CAT", img3);

	cv::waitKey();
	cv::destroyAllWindows();

}

void show6()
{   //for문을 이용한 픽셀
	cv::Mat img1 = cv::Mat::zeros(512, 512, CV_8UC1);   //검은색 빈 도화지 세팅
	uchar value = 0;    //at<uchar>(i, j):i번째 줄, j번째 칸에 있는 데이터를 uchar 타입으로 읽거나 쓰겠다
						//unchar은 0~255까지
	for(int i=0;i< img1.rows;++i)
	{
		for (int j = 0; j < img1.cols; ++j)  //i는 위에서 아래로 j는 왼쪽에서 오른쪽으로 검은색에서 흰색
		{
			++value;
			img1.at<uchar>(i, j) = value;     //value가 증가함 크기가 512이므로 255 두번반복된 그림출력
		}                                 
	}
	cv::namedWindow("IMAGE!!");
	cv::imshow("IMAGE!!", img1);
	cv::waitKey();
	cv::destroyAllWindows();
}

void show7()
{
	//이미지 속성 조회
	cv::Mat img1 = cv::imread("coins.png", cv::IMREAD_UNCHANGED);  //cv::IMREAD_UNCHANGED = 원본을 변하지 않게 그대로 가지고와
	if (img1.empty()) return;
	std::cout << "이미지의 폭 : " << img1.cols << std::endl;
	std::cout << "이미지의 높이 : " << img1.rows << std::endl;
	std::cout << "이미지의 사이즈 : " << img1.size << std::endl;
	std::cout << "픽셀 1개의 사이즈 : " << img1.elemSize() << std::endl;
	std::cout << "채널 : " << img1.channels() << std::endl;

	if (img1.type() == CV_8UC1) std::cout << "그레이" << std::endl;
	else if (img1.type() == CV_8UC3) std::cout << "컬러" << std::endl;
	else std::cout << "PNG" << std::endl;
}

void show8()
{	//행렬
	float data[] = { 1.0f, 2.0f,3.0f,4.0f, 5.0f, 6.0f};
	cv::Mat mat1(3, 3, CV_32FC1, data);
	cv::Mat mat2 = mat1.inv();
	cv::Mat mat3 = mat1* mat2;

	std::cout << mat1 << std::endl;
	std::cout << mat2 << std::endl;
	std::cout << mat3 << std::endl;

	uchar data2[] = { 1,2,3,4,5,6,7,8,9,10,11,12 };
	cv::Mat mat4(3, 4, CV_8UC1, data2);
	std::cout << mat4 << std::endl;
	cv::Mat mat5 = mat4.reshape(0, 4);  //(채널,ROW갯수)
	std::cout << mat5 << std::endl;

	//cv::Mat img1 = cv::imread("Lenna.png",cv::IMREAD_GRAYSCALE);
	//cv::namedWindow("Lenna");
	//cv::imshow("Lenna", img1);
	//cv::Mat img2 = img1 - 50;    //+50 더밝게 -50 더어둡게;
	//cv::namedWindow("Lenna2");
	//cv::imshow("Lenna2", img2);
	//cv::waitKey();
	//cv::destroyAllWindows();
}

void printMat(cv::InputArray _mat1)
{
	cv::Mat mat = _mat1.getMat();
	std::cout << mat << std::endl;
}
void InputArrayOf()
{
	uchar data1[] = { 1,2,3,4,5,6 };
	cv::Mat mat1(2, 3, CV_8U, data1);
	printMat(mat1);
}
void show9()
{
	InputArrayOf();
}
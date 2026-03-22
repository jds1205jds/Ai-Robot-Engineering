#include "opencv2/opencv.hpp"

void show20()
{
	//행렬 연산(+)='Saturation(포화) 연산 과 직접 픽셀 접근(at<uchar>)= 초과(Overflow)의 차이
	cv::Mat src = cv::imread("lenna.png", cv::IMREAD_GRAYSCALE);
	cv::Mat dst = src + 100;
	cv::Mat dst2(512,512,CV_8UC1);
	for (int i = 0; i < src.rows; ++i)
	{
		for (int j = 0; j < src.cols; ++j)
		{
			dst2.at<uchar>(i, j) = src.at<uchar>(i, j) + 100;
		}
	}
	cv::imshow("SRC", src);
	cv::imshow("DST", dst);
	cv::imshow("DST2", dst2);
	cv::waitKey();
	cv::destroyAllWindows();

}

void on_brightness(int position, void* userdata)
{
	std::cout << "Trackbar" << std::endl;
	cv::Mat src = *(cv::Mat*)userdata;
	cv::Mat dst = src + position;
	cv::imshow("DST", dst);
}
void show21()
{
	//트랙바를 이용한 명암조절
	cv::Mat src = cv::imread("lenna.png", cv::IMREAD_GRAYSCALE);
	cv::namedWindow("DST");
	cv::createTrackbar("Brightness", "DST", 0, 100, on_brightness, (void*)&src);
	cv::waitKey();
	cv::destroyAllWindows();

}

void show22()
{
	//명암조절공식(예쁘게 출력하는 공식)
	cv::Mat src = cv::imread("lenna.png", cv::IMREAD_GRAYSCALE);
	float alpha = 1.0f;
	cv::Mat dst = (1 + alpha) * src - 128 * alpha;
	cv::imshow("SRC", src);
	cv::imshow("DST", dst);
	cv::waitKey();
	cv::destroyAllWindows();
}

//히스토그램 - 뿌옇고 대비(Contrast)가 낮은 영상을 선명하게 만드는 핵심 기술
//cv::Mat dst;
//cv::normalize(src, dst, 0, 255, cv::NORM_MINMAX); 
////
//cv::equalizeHist(src, dst);
//등으로 대체 가능 
//원리: 영상에서 가장 어두운 값($min$)을 0으로, 가장 밝은 값($max$)을 255로 늘립니다.
//효과 : 뿌옇게 뭉쳐 있던 명암 차이가 커지면서 전체적인 대비(Contrast)가 살아납니다.
//특징 : 원래 히스토그램의 형태(비율)는 유지하면서 범위만 넓힙니다.
void show23()
{
	//히스토그램
	cv::Mat src = cv::imread("hawkes.bmp", cv::IMREAD_GRAYSCALE);
	double min, max = 0.0;
	cv::minMaxLoc(src, &min, &max);
	cv::Mat dst = (src - min) * 255 / (max - min);
	cv::imshow("SRC", src);
	cv::imshow("DST", dst);
	cv::waitKey();
	cv::destroyAllWindows();
}


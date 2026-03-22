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


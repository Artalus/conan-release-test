#include <iostream>
#include <boost/date_time/gregorian/gregorian.hpp>
#include "sometimes.h"

void sometimes(){
    using namespace std;

    cout << "Hello World! I am compiled in "
    #ifdef NDEBUG
        "Release!"
    #else
        "Debug!"
    #endif
    << endl;

    using namespace boost::gregorian;

    date today = day_clock::local_day();
    partial_date new_years_day(1,Jan);

    days days_since_year_start = today - new_years_day.get_date(today.year());
    cout << "Days since Jan 1: " << days_since_year_start.days() << endl;
    
    days days_until_year_start = new_years_day.get_date(today.year()+1) - today;
    cout << "Days until next Jan 1: " << days_until_year_start.days() << endl;
}

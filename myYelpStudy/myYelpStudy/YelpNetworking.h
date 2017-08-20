//
//  YelpNetworking.h
//  myYelpStudy
//
//  Created by Roger Ho on 19/06/2017.
//  Copyright © 2017 Chen. All rights reserved.
//

#import <Foundation/Foundation.h>
//#import "YelpDataModel.h"

@import CoreLocation;

typedef void (^RestaurantCompletionBlock)(NSArray <YelpDataModel *>* dataModelArray);

@interface YelpNetworking : NSObject

+ (YelpNetworking *)sharedInstance;

- (void)fetchRestaurantsBasedOnLocation:(CLLocation *)location term:(NSString *)term completionBlock:(RestaurantCompletionBlock)completionBlock;

@end

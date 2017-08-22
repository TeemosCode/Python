//
//  ViewController.m
//  tipCalculator
//
//  Created by Chen on 14/06/2017.
//  Copyright © 2017 Chen. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()



@property (weak, nonatomic) IBOutlet UITextField *textField;

@property (weak, nonatomic) IBOutlet UISegmentedControl *segmentControl;

@property (weak, nonatomic) IBOutlet UILabel *tipNum;

@property (weak, nonatomic) IBOutlet UILabel *totalAmount;

@end

@implementation ViewController

- (IBAction)didTapSegmentControl:(id)sender {
    [self updateValue];
}


- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)updateValue
{
    [self.view endEditing:YES];
    CGFloat billAmount = [self.textField.text floatValue];
    NSArray *tipValues = @[@(0.1),@(0.15),@(0.2)];
    CGFloat tip = billAmount * [tipValues[[self.segmentControl selectedSegmentIndex]] floatValue];
    self.tipNum.text = [NSString stringWithFormat:@"$%10.2f",tip];
    self.totalAmount.text = [NSString stringWithFormat:@"$%10.2f",tip + billAmount];
}



@end

@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    WelcomeComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    RouterModule.forRoot(routes)
  ],
  providers: [SequenceService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
